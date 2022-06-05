from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViews,SiteSettingsViews

router = DefaultRouter()

router.register(r'personalinfo', PersonalInfoViews, basename='personalinfo')
router.register(r'sitesettings', SiteSettingsViews, basename='sitesettings')

urlpatterns = [

] + router.urls
