from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    website = models.URLField(max_length=200, blank=True)
    twitter_handle = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
