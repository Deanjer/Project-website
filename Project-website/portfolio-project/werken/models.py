from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Werken(models.Model):
 title = models.CharField(max_length=200)
 body = models.TextField()
 url = models.TextField()
 pub_date = models.DateTimeField()
 image = models.ImageField(upload_to='media/images/', blank=True, null=True)
 icon = models.ImageField(upload_to='media/icon/', blank=True, null=True)
 votes_total = models.IntegerField(default=1)
 hunter = models.ForeignKey(User, on_delete=models.CASCADE)

  # admin panel
 def __str__(self):
    return self.title

 def summary(self):
    return self.body[:200]

# pub_date_pretty
