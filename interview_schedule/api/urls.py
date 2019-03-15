from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'candidate', views.CandidateViewSet)
router.register(r'interviewer', views.InterviewerViewSet)

urlpatterns = [
    path('', include(router.urls))
]