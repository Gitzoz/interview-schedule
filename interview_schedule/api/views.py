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
    lookup_url_kwarg = "candidate_id"

    def get_queryset(self):
        canidate_id = self.kwargs.get(self.lookup_url_kwarg)
        return CandidateAppointmentSlot.objects.filter(candidate = canidate_id)

    def perform_create(self, serializer):
        canidate_id = self.kwargs.get(self.lookup_url_kwarg)
        serializer.save(candidate=canidate_id)

class InterviewerAppointmentSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint for appointment slots
    """

    serializer_class = InterviewerAppointmentSlotSerializer
    lookup_url_kwarg = "interviewer_id"

    def get_queryset(self):
        interviewer_id = self.kwargs.get(self.lookup_url_kwarg)
        return InterviewerAppointmentSlot.objects.filter(interviewer = interviewer_id)

    def perform_create(self, serializer):
        interviewer_id = self.kwargs.get(self.lookup_url_kwarg)
        serializer.save(interviewer=interviewer_id)