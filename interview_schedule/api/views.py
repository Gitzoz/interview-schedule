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
    queryset = CandidateAppointmentSlot.objects.all()


class InterviewerAppointmentSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint for appointment slots
    """

    serializer_class = InterviewerAppointmentSlotSerializer
    lookup_url_kwarg = "interviewer_id"
    queryset = InterviewerAppointmentSlot.objects.all()