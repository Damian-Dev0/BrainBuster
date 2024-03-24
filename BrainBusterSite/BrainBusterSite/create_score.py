from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from BrainBusterApp.models import Score

@receiver(post_save, sender=User)
def create_user_score(sender, instance, created, **kwargs):
    if created:
        # Create an instance of Score for new User
        Score.objects.create(User_ID=instance.id, Points=0)
