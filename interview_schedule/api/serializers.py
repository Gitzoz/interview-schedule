from .models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'created_at')

class CandidateSerializer(UserSerializer):
    pass

class InterviewerSerializer(UserSerializer):
    pass

class AppointmentSlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppointmentSlot
        fields = ('begin', 'end', 'user')
