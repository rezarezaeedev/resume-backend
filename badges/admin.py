from django.contrib import admin
from .models import Skill,Experience,InterestGroup,InterestBadge

@admin.register(Skill)
class AdminSkills(admin.ModelAdmin):
    pass

@admin.register(Experience)
class AdminExperience(admin.ModelAdmin):
    pass

@admin.register(InterestGroup)
class AdminInterestGroup(admin.ModelAdmin):
    pass

@admin.register(InterestBadge)
class AdminInterestBadge(admin.ModelAdmin):
    pass
