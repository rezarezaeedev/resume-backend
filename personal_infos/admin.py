from django.contrib import admin
from .models import PersonalInfo,SiteSettings

@admin.register(PersonalInfo)
class AdminPersonalInfo(admin.ModelAdmin):
    list_display = ['id','name','job_title']
    list_display_links =  list_display

@admin.register(SiteSettings)
class AdminSiteSettings(admin.ModelAdmin):
    list_display = ['id', 'copyright_text','builded_text']
    list_display_links =  list_display


