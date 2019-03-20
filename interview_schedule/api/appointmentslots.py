from .models import *


def calculateAppointmentSlotOverlaps(interviewerIds, candidateId):
    candidateSlots = CandidateAppointmentSlot.objects.filter(candidate=candidateId)
    interviewerSlots = InterviewerAppointmentSlot.objects.filter(interviewer__in=interviewerIds)

    result = []
    for candidateSlot in candidateSlots:
        overlappingInterviewerSlots = list(
            filter(lambda interviewerSlot: dateRangeIsInDateRange(candidateSlot, interviewerSlot), interviewerSlots)
        )
        result.append((candidateSlot, overlappingInterviewerSlots))

    return result


def dateRangeIsInDateRange(a, b):
    return (a.begin <= b.begin) and (a.end >= b.end)
