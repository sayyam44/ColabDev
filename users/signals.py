from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings
# sender - It is the model that sends this action 
# instance - Instance of the model that triggers this
#created - it returns the true or false on the basis whether the action has occured or not
# @receiver(post_save,sender=Profile) #using decorators here

#the below function creates a new profile as soon as a new user is added into the system
def createProfile(sender, instance, created, **kwargs):
    print('Profile saved')
    # print("Instance:",instance)
    # print('CREATED', created)
    if created:
        user=instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject= 'Welcome To ColabDev'
        message = 'We are glad you are here! Lets connect with Developers worldwide.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender,instance,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass
#This means anytime the save method id called on the Profile model 
#after the save method is called we will be able to make changes on the model
post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)