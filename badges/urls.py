from django.urls import path
from .views import SkillView, ExperienceView, InterestGroupView,InterestBadgeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'skills', SkillView, basename='skills')
router.register(r'experiences', ExperienceView, basename='experiences')
router.register(r'interestgroups', InterestGroupView, basename='interestgroups')
router.register(r'interestbadges', InterestBadgeView, basename='interestbadges')

urlpatterns = [

] + router.urls
