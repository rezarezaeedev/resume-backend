# Generated by Django 4.0.4 on 2022-06-04 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0012_interestbadge_order_skill_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='order',
            field=models.SmallIntegerField(blank=1, default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interestgroup',
            name='order',
            field=models.SmallIntegerField(blank=1, default='1'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interestbadge',
            name='order',
            field=models.SmallIntegerField(blank=1),
        ),
        migrations.AlterField(
            model_name='skill',
            name='order',
            field=models.SmallIntegerField(blank=1),
        ),
    ]
