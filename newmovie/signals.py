from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from .models import UserMine

def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)
        UserMine.objects.create(
            user=instance,
            name=instance.username
        )
        print('profile created')
post_save.connect(user_profile, sender=User)