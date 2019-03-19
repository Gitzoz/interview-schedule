from .models import *


def calculateAppointmentSlotOverlaps(interviewerId, candidateId):
    candidateSlots = CandidateAppointmentSlot.objects.filter(candidate=candidateId)
    interviewerSlots = InterviewerAppointmentSlot.objects.filter(interviewer=interviewerId)

    result = []
    for interviewerSlot in interviewerSlots:
        overlappingCandidateSlots = list(
            filter(lambda candidateslot: dateRangeIsInDateRange(interviewerSlot, candidateslot), candidateSlots)
        )
        result.append((interviewerSlot, overlappingCandidateSlots))

    return result


def dateRangeIsInDateRange(a, b):
    return (a.begin <= b.begin) and (a.end >= b.end)
