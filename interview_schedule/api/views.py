from .serializers import *
from .exceptions import QueryParameterException
from rest_framework import viewsets
from rest_framework.response import Response
from .appointmentslots import calculateAppointmentSlotOverlaps


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


class AppointmentOverlapViewSet(viewsets.ViewSet):
    candidateIdParam = "candidateId"
    interviewerIdsParam = "interviewerIds"

    def list(self, request):
        candidateId = request.query_params.get(self.candidateIdParam, None)
        interviewerIdParamValue = request.query_params.get(self.interviewerIdsParam, None)
        if interviewerIdParamValue is None:
            raise QueryParameterException('There was no interviewerIds provided via query parameter')
        if candidateId is None:
            raise QueryParameterException('There was no candidateId provided via query parameter')

        try:
            interviewerIds = [ int(x) for x in interviewerIdParamValue.split(',') ]
        except:
            raise QueryParameterException('interviewerIds must be a comma separated list of integers')

        result = calculateAppointmentSlotOverlaps(interviewerIds, candidateId)
        return Response(serializeAppointmentOverlapResult(result))
