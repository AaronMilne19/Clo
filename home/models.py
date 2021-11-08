from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Magazine(models.Model):

    title = models.CharField(max_length=300, unique=True)
    description_short = models.CharField(max_length=600)
    description_long = models.CharField(max_length=1200)
    price = models.IntegerField(default = 0 )
    discount = models.IntegerField(default=0)
    photo1 = models.ImageField(upload_to='magazine_pictures', blank=True, default = None)
    photo2 = models.ImageField(upload_to='magazine_pictures', blank=True, default=None)
    link_to_publishers_site = models.URLField(max_length=300)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    #Links UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    #The other attributes to include for the user
    email = models.CharField(max_length = 254)
    username = models.CharField(max_length = 30)

    picture = models.ImageField(upload_to='profile_pictures', blank=True, default = None, null=True)


    def __str__(self):
        return self.username


