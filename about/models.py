from django.db import models
from taggit.managers import TaggableManager
from icon_color_tags.models import TaggedThing


class WebDesigning(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField()
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.DateField(auto_now=False, auto_now_add=False)
    project_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class SoftwareDevelopment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.DateField(auto_now=False, auto_now_add=False)
    project_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class MachineLearning(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.DateField(auto_now=False, auto_now_add=False)
    project_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name
