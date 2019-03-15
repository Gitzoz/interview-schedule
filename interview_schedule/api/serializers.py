from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'created_at')
        read_only_fields = ('id',)

class CandidateSerializer(UserSerializer):
    pass

class InterviewerSerializer(UserSerializer):
    pass

class InterviewerAppointmentSlotSerializer(serializers.HyperlinkedModelSerializer):
    interviewer = serializers.PrimaryKeyRelatedField(queryset=Interviewer.objects.all())
    class Meta:
        model = InterviewerAppointmentSlot
        fields = ('id', 'begin', 'end', 'interviewer')
        read_only_fields = ('id',)


class CandidateAppointmentSlotSerializer(serializers.HyperlinkedModelSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    class Meta:
        model = CandidateAppointmentSlot
        fields = ('id', 'begin', 'end', 'candidate')
        read_only_fields = ('id',)