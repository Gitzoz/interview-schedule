from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)
router.register(r'candidate/appointmentslots', views.CandidateAppointmentSlotViewSet, base_name='candidate-appointmentslots')
router.register(r'interviewers', views.InterviewerViewSet)
router.register(r'interviewer/appointmentslots', views.InterviewerAppointmentSlotViewSet, base_name='interviewer-appointmentslots')
router.register(r'appointments/overlap', views.AppointmentOverlapViewSet, base_name='appointments-overlap')

urlpatterns = [
    path('', include(router.urls)),
]