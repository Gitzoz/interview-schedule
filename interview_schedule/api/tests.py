from django.test import TestCase
from .models import *
from .validators import *
from .appointmentslots import calculateAppointmentSlotOverlaps
import datetime


class ValidationTestCase(TestCase):
    def test_begin_must_before_end(self):
        begin = datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M')
        end = datetime.datetime.strptime('2018-06-28T08:15', '%Y-%m-%dT%H:%M')
        self.assertRaises(serializers.ValidationError, beginIsBeforeEnd, begin, end)

    def test_begin_is_before_end(self):
        end = datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M')
        begin = datetime.datetime.strptime('2018-06-28T08:15', '%Y-%m-%dT%H:%M')
        result = beginIsBeforeEnd(begin, end)
        self.assertEqual(True, result)

    def test_date_must_be_at_full_hour(self):
        date = datetime.datetime.strptime('2018-06-29T08:15', '%Y-%m-%dT%H:%M')
        self.assertRaises(serializers.ValidationError, mustBeAtFullHour, date)

    def test_date_is_at_full_hour(self):
        date = datetime.datetime.strptime('2018-06-29T08:00', '%Y-%m-%dT%H:%M')
        self.assertEqual(mustBeAtFullHour(date), date)


class AppointmentSlotOverlapTest(TestCase):
    begin1 = datetime.datetime.strptime('2018-06-28T08:00', '%Y-%m-%dT%H:%M')
    end1 = datetime.datetime.strptime('2018-06-30T08:00', '%Y-%m-%dT%H:%M')
    begin2 = datetime.datetime.strptime('2018-06-28T08:00', '%Y-%m-%dT%H:%M')
    end2 = datetime.datetime.strptime('2018-06-29T08:00', '%Y-%m-%dT%H:%M')
    begin3 = datetime.datetime.strptime('2018-06-27T08:00', '%Y-%m-%dT%H:%M')
    end3 = datetime.datetime.strptime('2018-06-30T08:00', '%Y-%m-%dT%H:%M')
    candidateId = None
    interviewerId = None
    expectedInterviewerSlot = None
    expectedCandidateSlot = None

    def setUp(self):
        interviewer = Interviewer.objects.create(name='Interviewer1')
        self.interviewerId = interviewer.id
        candidate = Candidate.objects.create(name='Candidate1')
        self.candidateId = candidate.id
        self.expectedInterviewerSlot = InterviewerAppointmentSlot.objects.create(begin=self.begin2, end=self.end2, interviewer=interviewer)
        CandidateAppointmentSlot.objects.create(begin=self.begin1, end=self.end1, candidate=candidate)
        self.expectedCandidateSlot = CandidateAppointmentSlot.objects.create(begin=self.begin2, end=self.end2, candidate=candidate)
        CandidateAppointmentSlot.objects.create(begin=self.begin3, end=self.end3, candidate=candidate)

    def test_only_the_overlapping_slot_is_shown(self):
        overlap = calculateAppointmentSlotOverlaps(self.interviewerId, self.candidateId)
        expected = [(self.expectedInterviewerSlot, [self.expectedCandidateSlot])]
        self.assertEqual(overlap, expected)
