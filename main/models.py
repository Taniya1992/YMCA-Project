from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username1 = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, blank=True)
    # Date_of_birth = models.DateField()
    Contact_Number = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    Address = models.TextField()

    def __str__(self):
        return self.user.username

class Programs_category(models.Model):
    Program_category_name = models.CharField(max_length=1000)
    Program_Description = models.CharField(max_length=10000)
    Program_logo = models.FileField(upload_to='media')


    def __str__(self):
        return self.Program_category_name



bolean_CHOICES = [('Active', 'Active'),('Cancel', 'Cancel'),]
      
class Programs(models.Model):
    Programs_category_name = models.CharField(max_length=1000)
    Program_name = models.CharField(max_length=1000)
    Price_for_ymca_Member = models.CharField(max_length=1000)
    Price_for_non_ymca_Member = models.CharField(max_length=1000)
    StartingDate = models.DateField(max_length=1000)
    EndingDate = models.DateField(max_length=1000)
    StartingTime =  models.TimeField()
    EndingTime = models.TimeField()
    Location = models.TextField(max_length=1000)
    Description = models.TextField(max_length=1000)
    Participant_allowed = models.IntegerField()
    status = models.CharField(choices=bolean_CHOICES,default='Active',max_length=100)

    def __str__(self):
        return self.Program_name

class Register(models.Model):
    User = models.CharField(max_length=1000)
    Program_name = models.CharField(max_length=1000)
    Price = models.CharField(max_length=1000)
    Date = models.CharField(max_length=1000)
    Time = models.CharField(max_length=1000)
    status = models.CharField(choices=bolean_CHOICES,default='Active',max_length=100)

    def __str__(self):
        return self.User


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()