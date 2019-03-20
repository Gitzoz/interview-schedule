from django.test import TestCase
from django.utils.timezone import make_aware
from .models import *
from .validators import *
from .appointmentslots import calculateAppointmentSlotOverlaps
import datetime



class ValidationTestCase(TestCase):
    def test_begin_must_before_end(self):
        begin = make_aware(datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M'))
        end = make_aware(datetime.datetime.strptime('2018-06-28T08:15', '%Y-%m-%dT%H:%M'))
        self.assertRaises(serializers.ValidationError, beginIsBeforeEnd, begin, end)

    def test_begin_is_before_end(self):
        end = make_aware(datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M'))
        begin = make_aware(datetime.datetime.strptime('2018-06-28T08:15', '%Y-%m-%dT%H:%M'))
        result = beginIsBeforeEnd(begin, end)
        self.assertEqual(True, result)

    def test_date_must_be_at_full_hour(self):
        date = make_aware(datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M'))
        self.assertRaises(serializers.ValidationError, mustBeAtFullHour, date)

    def test_date_is_at_full_hour(self):
        date = make_aware(datetime.datetime.strptime('2018-06-29T08:00', '%Y-%m-%dT%H:%M'))
        self.assertEqual(mustBeAtFullHour(date), date)


class AppointmentSlotOverlapTest(TestCase):
    begin1 = make_aware(datetime.datetime.strptime('2018-06-28T08:00', '%Y-%m-%dT%H:%M'))
    end1 = make_aware(datetime.datetime.strptime('2018-06-30T08:00', '%Y-%m-%dT%H:%M'))
    begin2 = make_aware(datetime.datetime.strptime('2018-06-28T08:00', '%Y-%m-%dT%H:%M'))
    end2 = make_aware(datetime.datetime.strptime('2018-06-29T08:00', '%Y-%m-%dT%H:%M'))
    begin3 = make_aware(datetime.datetime.strptime('2018-06-27T08:00', '%Y-%m-%dT%H:%M'))
    end3 = make_aware(datetime.datetime.strptime('2018-06-30T08:00', '%Y-%m-%dT%H:%M'))
    candidateId = None
    interviewerId1 = None
    interviewerId2 = None
    expectedInterviewer1Slot = None
    expectedInterviewer2Slot = None
    expectedCandidateSlot = None

    def setUp(self):
        interviewer1 = Interviewer.objects.create(name='Interviewer1')
        self.interviewerId1 = interviewer1.id

        interviewer2 = Interviewer.objects.create(name='Interviewer2')
        self.interviewerId2 = interviewer2.id

        candidate = Candidate.objects.create(name='Candidate1')
        self.candidateId = candidate.id

        self.expectedCandidateSlot = CandidateAppointmentSlot.objects.create(begin=self.begin2, end=self.end2, candidate=candidate)

        InterviewerAppointmentSlot.objects.create(begin=self.begin1, end=self.end1, interviewer=interviewer1)
        self.expectedInterviewer1Slot = InterviewerAppointmentSlot.objects.create(begin=self.begin2, end=self.end2, interviewer=interviewer1)
        InterviewerAppointmentSlot.objects.create(begin=self.begin3, end=self.end3, interviewer=interviewer1)

        InterviewerAppointmentSlot.objects.create(begin=self.begin1, end=self.end1, interviewer=interviewer2)
        self.expectedInterviewer2Slot = InterviewerAppointmentSlot.objects.create(begin=self.begin2, end=self.end2, interviewer=interviewer2)
        InterviewerAppointmentSlot.objects.create(begin=self.begin3, end=self.end3, interviewer=interviewer2)

    def test_only_the_overlapping_slot_is_shown_with_one_interviewers(self):
        overlap = calculateAppointmentSlotOverlaps([self.interviewerId1], self.candidateId)
        expected = [(self.expectedCandidateSlot, [self.expectedInterviewer1Slot])]
        self.assertEqual(overlap, expected)

    def test_only_the_overlapping_slot_is_shown_with_two_interviewers(self):
        overlap = calculateAppointmentSlotOverlaps([self.interviewerId1, self.interviewerId2], self.candidateId)
        expected = [(self.expectedCandidateSlot, [self.expectedInterviewer1Slot, self.expectedInterviewer2Slot])]
        self.assertEqual(overlap, expected)
