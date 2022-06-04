from django.contrib import admin
from .models import Skill,Experience,InterestGroup,InterestBadge

@admin.register(Skill)
class AdminSkills(admin.ModelAdmin):
    list_display = ['id','name','is_active', 'is_familiarity']
    list_display_links = list_display

@admin.register(InterestGroup)
class AdminInterestGroup(admin.ModelAdmin):
    list_display = ['id','name','is_active' ]
    list_display_links = list_display

@admin.register(InterestBadge)
class AdminInterestBadge(admin.ModelAdmin):
    list_display = ['id','name','is_active', 'group']
    list_display_links = list_display


@admin.register(Experience)
class AdminExperience(admin.ModelAdmin):
    list_display = ['id','position','company', 'location', 'starting_date','ending_date', ]
    list_display_links = list_display

