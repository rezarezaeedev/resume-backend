# Generated by Django 4.0.4 on 2022-05-31 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0006_alter_interestbadge_description_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='related_website',
            field=models.URLField(default='#'),
        ),
    ]
