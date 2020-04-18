from django.db import models
from taggit.managers import TaggableManager
from icon_color_tags.models import TaggedThing


class WebDesigning(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)
    project_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class SoftwareDevelopment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)
    project_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class MachineLearning(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)
    project_link = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)
    details = models.CharField(max_length=500, blank=True)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.company_name


class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name


class PersonalDetail(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    about = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
