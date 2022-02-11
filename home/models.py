from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
import datetime


class Magazine(models.Model):

    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=100, unique=True)
    description_short = models.CharField(max_length=1000)

    #long - in case we have seperate pages for each magzine
    description_long = models.CharField(max_length=2000)
    cover = models.ImageField(upload_to='magazine_pictures', default = None)
    link_to_publishers_site = models.URLField(max_length=300)
    #slug - again, in case we have seperate pages for each magzine
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Magazine, self).save(*args, **kwargs)


class MagazineIssue (models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    title = models.CharField(max_length =1000, default="No title", unique=True)
    issue_description = models.CharField(max_length=1000)
    price = models.IntegerField(default = 0 )
    discounted_price = models.IntegerField(default= 0)
    cover = models.ImageField(upload_to='magazine_pictures/', default=None)
    description_short = models.CharField(max_length=1000, default=None, null=True)
    date =  models.DateField(("Date"), default=datetime.date.today)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MagazineIssue, self).save(*args, **kwargs)


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_issues = models.ManyToManyField(MagazineIssue, related_name="saves")

    def __str__(self):
        return self.user.username


class Hashtag(models.Model):
    text = models.CharField(max_length=20)
    magazines = models.ManyToManyField(Magazine)

    def __str__(self):
        return self.text
