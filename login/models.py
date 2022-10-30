from enum import unique
from operator import mod
from random import choices
from django.db import models
from matplotlib.pyplot import cla, title
from django.contrib.auth.models import User
from traitlets import default

STATUS=((0,'Draft'),(1,'Publish'))
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content=models.TextField()
    data_created=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE)
    status= models.IntegerField(choices=STATUS,default=0)

    def __str__(self):
        return self.title
