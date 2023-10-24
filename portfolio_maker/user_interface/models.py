from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Information(models.Model):
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    about = models.CharField(blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)
    CV = models.FileField(upload_to="cv/", blank=True, null=True)
    fewWords = models.CharField(max_length=500, blank=True, null=True)

    #social_network
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    other = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.firstname
    
# class Education(models.Model):

