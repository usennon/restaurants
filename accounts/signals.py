from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('User profile is created')

    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()

        except:
            UserProfile.objects.create(user=instance)
            print("User profile was not exist, but i created one")

        print('User is updated')


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')
