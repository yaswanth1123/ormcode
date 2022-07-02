from nturl2path import url2pathname
from django.db import models

# Create your models here.
class Topic(models.Model):
    Topic_name=models.CharField(max_length=100,primary_key=True)
class Webpages(models.Model):
    Topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Player_name=models.CharField(max_length=100)
    URL=models.URLField()

class Access_Records(models.Model):
    Player_name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
