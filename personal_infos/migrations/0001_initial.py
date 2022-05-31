# Generated by Django 4.0.4 on 2022-05-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Enter your fullname')),
                ('job_title', models.CharField(max_length=30)),
                ('summary', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=30)),
                ('profile', models.ImageField(upload_to='')),
                ('phone', models.CharField(max_length=11)),
                ('whatsapp', models.CharField(max_length=11)),
                ('telegram', models.CharField(max_length=20)),
                ('linkedin', models.CharField(max_length=20)),
                ('github', models.CharField(max_length=20)),
                ('instagram', models.CharField(max_length=20)),
                ('copyright_text', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=0)),
            ],
        ),
    ]
