from django.db import models

# Create your models here.
class Badge(models.Model):
    '''
    An abstract class for inheriting common fields
    '''
    name = models.CharField(max_length=25, verbose_name='Skills name')
    description = models.CharField(max_length=50, verbose_name='A short description for this skills')
    description_link = models.URLField(default='')

    class Meta:
        abstract = True

class Skill(Badge):
    is_familiarity = models.BooleanField(default=False)

class InterestGroup(Badge):
    name = models.CharField(max_length=25, verbose_name='Interest name')
    description = models.CharField(max_length=50, verbose_name='A short description for this interest')

class InterestBadge(Badge):
    group = models.ForeignKey(InterestGroup, on_delete=models.CASCADE)


class Experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    rule_description = models.TextField()
    location = models.CharField(max_length=20, default='At home(remote)')
    starting_date = models.DateField()
    ending_date = models.DateField()
    related_website = models.URLField(default='')
