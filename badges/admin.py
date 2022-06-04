from django.contrib import admin
from .models import Skill,Experience,InterestGroup,InterestBadge

@admin.register(Skill)
class AdminSkills(admin.ModelAdmin):
    list_display = ['order','name','is_active', 'is_familiarity', 'id']
    list_display_links = list_display
    ordering = ['order','name','id']

@admin.register(InterestGroup)
class AdminInterestGroup(admin.ModelAdmin):
    list_display = ['order','name','is_active' , 'id']
    list_display_links = list_display
    ordering = ['order','name','id']

@admin.register(InterestBadge)
class AdminInterestBadge(admin.ModelAdmin):
    list_display = ['order','name','is_active', 'group', 'id']
    list_display_links = list_display
    ordering = ['order','name','id']


@admin.register(Experience)
class AdminExperience(admin.ModelAdmin):
    list_display = ['order','position','company', 'location', 'starting_date','ending_date', 'id']
    list_display_links = list_display
    ordering = ['order','position','company', 'location','id']

