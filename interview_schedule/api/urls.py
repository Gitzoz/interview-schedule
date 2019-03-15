from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'candidate', views.CandidateViewSet)
router.register(r'appointmentslots/candidate', views.CandidateAppointmentSlotViewSet, base_name='candidate-appointmentslots')
router.register(r'interviewer', views.InterviewerViewSet)
router.register(r'appointmentslots/interviewer', views.InterviewerAppointmentSlotViewSet, base_name='interviewer-appointmentslots')

urlpatterns = [
    path('', include(router.urls))
]