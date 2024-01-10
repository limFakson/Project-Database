from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=350)
    image = models.ImageField()


class AboutData(models.Model):
    syntax = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField()
