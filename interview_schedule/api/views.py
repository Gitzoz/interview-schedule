from django.http import HttpResponse
from .serializers import *
from rest_framework import  viewsets

import datetime


# Create your views here.
def index(request):
    return HttpResponse("Api is running")


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