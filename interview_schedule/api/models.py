from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField('user created at')

class Candidate(User):
    pass

class Interviewer(User):
    pass


class AppointmentSlot(models.Model):
    begin = models.DateTimeField('appointment start')
    end = models.DateTimeField('appointment end')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
