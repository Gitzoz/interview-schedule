from django.urls import path, include
from . import views
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Interview Schedule API",
        default_version='v0.0.1',
    ),
    public=True,
)


router = routers.DefaultRouter()
router.register(r'candidates', views.CandidateViewSet)
router.register(r'candidate/appointmentslots', views.CandidateAppointmentSlotViewSet, base_name='candidate-appointmentslots')
router.register(r'interviewers', views.InterviewerViewSet)
router.register(r'interviewer/appointmentslots', views.InterviewerAppointmentSlotViewSet, base_name='interviewer-appointmentslots')
router.register(r'appointments/overlap', views.AppointmentOverlapViewSet, base_name='appointments-overlap')

urlpatterns = [
    path('', include(router.urls)),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]