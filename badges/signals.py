from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Skill,Experience,InterestGroup,InterestBadge

@receiver(pre_save )
def set_order(sender,instance, *args, **kwargs):
    klass = instance.__class__

    if  klass in [Skill,Experience,InterestGroup,InterestBadge]:
        queryset = klass.objects.all().order_by('order').last()
        if queryset!=None and queryset!=instance:
            instance.order=queryset.order+1
        else:
            instance.order=1
