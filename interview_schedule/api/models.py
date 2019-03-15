from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('user created at', auto_now_add=True)

class Candidate(User):
    pass

class Interviewer(User):
    pass


class AppointmentSlot(models.Model):
    id = models.AutoField(primary_key=True)
    begin = models.DateTimeField('appointment start')
    end = models.DateTimeField('appointment end')


class CandidateAppointmentSlot(AppointmentSlot):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

class InterviewerAppointmentSlot(AppointmentSlot):
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
