from .models import *
from rest_framework import serializers
from .validators import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'created_at')
        read_only_fields = ('id',)

class CandidateSerializer(UserSerializer):
    pass

class InterviewerSerializer(UserSerializer):
    pass

class AppointmentSlotSerializer(serializers.HyperlinkedModelSerializer):
    begin = serializers.DateTimeField(validators=[mustBeAtFullHour])
    end = serializers.DateTimeField(validators=[mustBeAtFullHour])

    def validate(self, data):
        beginIsBeforeEnd(data)

class InterviewerAppointmentSlotSerializer(AppointmentSlotSerializer):
    interviewer = serializers.PrimaryKeyRelatedField(queryset=Interviewer.objects.all())
    class Meta:
        model = InterviewerAppointmentSlot
        fields = ('id', 'begin', 'end', 'interviewer')
        read_only_fields = ('id',)


class CandidateAppointmentSlotSerializer(AppointmentSlotSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    class Meta:
        model = CandidateAppointmentSlot
        fields = ('id', 'begin', 'end', 'candidate')
        read_only_fields = ('id',)