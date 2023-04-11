from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICE = (
    ('All','All'),
    ('Kids','Kids'),
)
MOVIE_CHOICES = (
    ('seasonal','Seasonal'),
    ('single','Single'),
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile',blank=True,null=True)
    
class Profile(models.Model):
    name = models.CharField(max_length=150)
    age_limit = models.CharField(choices=AGE_CHOICE,max_length=15)
    uuid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return self.name
    
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(choices=MOVIE_CHOICES,max_length=20)
    video = models.ManyToManyField('Video')
    image = models.ImageField(upload_to='covers')
    age_limit = models.CharField(choices=AGE_CHOICE,max_length=15)
    
    def __str__(self):
        return self.title
    
class Video(models.Model):
    title = models.CharField(max_length=20)
    file = models.FileField(upload_to='movies')
    
    def __str__(self):
        return self.title
    


