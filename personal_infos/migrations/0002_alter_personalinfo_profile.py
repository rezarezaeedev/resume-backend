# Generated by Django 4.0.4 on 2022-06-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_infos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='profile',
            field=models.ImageField(upload_to='profiles'),
        ),
    ]
