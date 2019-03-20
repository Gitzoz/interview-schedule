from .models import *
from rest_framework import serializers
from .validators import *

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'name', 'created_at')
        read_only_fields = ('id',)

class InterviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviewer
        fields = ('id', 'name', 'created_at')
        read_only_fields = ('id',)

class AppointmentSlotSerializer(serializers.ModelSerializer):
    def validate(self, data):
        beginIsBeforeEnd(data['begin'], data['end'])
        return data

class InterviewerAppointmentSlotSerializer(AppointmentSlotSerializer):
    interviewer = serializers.PrimaryKeyRelatedField(queryset=Interviewer.objects.all())
    begin = serializers.DateTimeField(validators=[mustBeAtFullHour])
    end = serializers.DateTimeField(validators=[mustBeAtFullHour])

    class Meta:
        model = InterviewerAppointmentSlot
        fields = ('id', 'begin', 'end', 'interviewer')
        read_only_fields = ('id',)


class CandidateAppointmentSlotSerializer(AppointmentSlotSerializer):
    candidate = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.all())
    begin = serializers.DateTimeField(validators=[mustBeAtFullHour])
    end = serializers.DateTimeField(validators=[mustBeAtFullHour])

    class Meta:
        model = CandidateAppointmentSlot
        fields = ('id', 'begin', 'end', 'candidate')
        read_only_fields = ('id',)


def serializeAppointmentOverlapResult(data):
    serialized = []
    for dataTuple in data:
        interviewerSlotSerializer = InterviewerAppointmentSlotSerializer(dataTuple[1], many=True)
        candidateSlotsSerializer = CandidateAppointmentSlotSerializer(dataTuple[0])
        serialized.append({'candidate-slot': candidateSlotsSerializer.data, 'interviewer-slots': interviewerSlotSerializer.data})

    return serialized