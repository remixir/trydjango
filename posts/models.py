from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120) #max_length=120
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False) #auto_now all single time save in datebase
    timestamp =  models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    # def __unicode__(self): // 1.8 zwraca nazwe modelu
    #     return self.titled

