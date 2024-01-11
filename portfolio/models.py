from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=350)
    image = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=200)


class AboutData(models.Model):
    syntax = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
