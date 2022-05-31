from django.urls import path
from .views import SkillView, ExperienceView, InterestGroupView,InterestBadgeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'skills', SkillView, basename='skills')
router.register(r'experiences', ExperienceView, basename='experiences')
router.register(r'interestgroup', InterestGroupView, basename='interestgroup')
router.register(r'interestbadge', InterestBadgeView, basename='interestbadge')

urlpatterns = [

] + router.urls
