from django.db.models.signals import post_save
from django.dispatch import receiver
from usage.models import DailyUsage
from .utils import calculate_daily_report

@receiver(post_save, sender=DailyUsage)
def update_daily_report(sender, instance, **kwargs):
    calculate_daily_report(instance.date)
