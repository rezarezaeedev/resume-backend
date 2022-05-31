from django.urls import path
from .views import PersonalInfoViews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'personalinfo', PersonalInfoViews, basename='personalinfo')

urlpatterns = [

] + router.urls
