from django.contrib import admin
from .models import PersonalInfo

@admin.register(PersonalInfo)
class AdminPersonalInfo(admin.ModelAdmin):
    list_display = ['id','name','job_title']
