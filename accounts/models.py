from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save

# Create your models here.

# User model

class User(AbstractUser):

    phone=models.CharField(max_length=10,unique=True)

    ROLE_CHOICES=(
        ("tutor","Tutor"),
        ("student","Student")
    )

    role= models.CharField(choices=ROLE_CHOICES,default="student",max_length=200)

# Trainer model
class TrainerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="trainer_profile",
    )
    bio = models.TextField(blank=True,null=True)
    expertise = models.CharField(max_length=255, blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    organization = models.CharField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TrainerProfile: {self.user.username}"

# Student model

class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    bio = models.TextField(blank=True,null=True)
    education = models.CharField(max_length=255, blank=True,null=True)
    skills = models.CharField(max_length=255, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"StudentProfile: {self.user.username}"

#signals 

def create_trainer_profile(sender,instance,created,**kwargs):

    if created and instance.role=="tutor":

        TrainerProfile.objects.create(user=instance)

def create_student_profile(sender,instance,created,**kwargs):

    if created and instance.role=="student":

        StudentProfile.objects.create(user=instance)

post_save.connect(create_trainer_profile,sender=User)
post_save.connect(create_student_profile,sender=User)

    


