from django.db import models
from django.conf import settings

def image_upload_path():
    result = f'profiles'
    return result

class PersonalInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='Enter your fullname')
    persian_name = models.CharField(max_length=30, verbose_name='نام خود را به فارسی وارد کنید')
    job_title = models.CharField(max_length=30)
    summary = models.TextField()
    address = models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    profile_image = models.ImageField(upload_to=image_upload_path())
    phone = models.CharField(max_length=11)
    whatsapp = models.CharField(max_length=11)
    telegram = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=20)
    github = models.CharField(max_length=20)
    instagram = models.CharField(max_length=20)
    is_active=models.BooleanField(default=0)


class SiteSettings(models.Model):
    copyright_text = models.CharField(max_length=100)
    builded_text = models.CharField(max_length=100)
    is_active=models.BooleanField(default=0)
