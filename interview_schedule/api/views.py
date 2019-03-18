from .serializers import *
from rest_framework import  viewsets


class CandidateViewSet(viewsets.ModelViewSet):
    """
    API endpoint for candidates
    """
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class InterviewerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for interviewers
    """
    queryset = Interviewer.objects.all()
    serializer_class = InterviewerSerializer

class CandidateAppointmentSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint for appointment slots
    """
    serializer_class = CandidateAppointmentSlotSerializer
    candidateIdParam = "candidateId"

    def get_queryset(self):
        queryset = CandidateAppointmentSlot.objects.all()
        candidateId = self.request.query_params.get(self.candidateIdParam, None)
        if candidateId is not None:
            queryset = queryset.filter(candidate=candidateId)
        return queryset


class InterviewerAppointmentSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint for appointment slots
    """
    serializer_class = InterviewerAppointmentSlotSerializer
    interviewerIdParam = "interviewerId"

    def get_queryset(self):
        queryset = InterviewerAppointmentSlot.objects.all()
        interviewerId = self.request.query_params.get(self.interviewerIdParam, None)
        if interviewerId is not None:
            queryset = queryset.filter(candidate=interviewerId)
        return queryset