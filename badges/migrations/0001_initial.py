# Generated by Django 4.0.4 on 2022-05-31 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('rule_description', models.TextField()),
                ('location', models.CharField(default='At home(remote)', max_length=20)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('related_website', models.URLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='InterestGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_link', models.URLField(default='')),
                ('name', models.CharField(max_length=25, verbose_name='Interest name')),
                ('description', models.CharField(max_length=50, verbose_name='A short description for this interest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Skills name')),
                ('description', models.CharField(max_length=50, verbose_name='A short description for this skills')),
                ('description_link', models.URLField(default='')),
                ('is_familiarity', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterestBadge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Skills name')),
                ('description', models.CharField(max_length=50, verbose_name='A short description for this skills')),
                ('description_link', models.URLField(default='')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badges.interestgroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]