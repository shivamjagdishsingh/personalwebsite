from django.db import models
from taggit.managers import TaggableManager
from icon_color_tags.models import TaggedThing
import os


def get_upload_path(instance, filename):
    return os.path.join(
        "%s" % instance.name.replace(' ', ''), filename)


class WebDesigning(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)
    project_link = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    video = models.FileField(upload_to=get_upload_path, null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.name


class SoftwareDevelopment(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)
    project_link = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    video = models.FileField(upload_to=get_upload_path, null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.name


class MachineLearning(models.Model):
    name = models.CharField(max_length=50, blank=True)
    desc = models.CharField(max_length=500, blank=True)
    tags = TaggableManager(through=TaggedThing)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.CharField(max_length=500, blank=True)
    project_link = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to=get_upload_path, blank=True, null=True)
    video = models.FileField(upload_to=get_upload_path, null=True, blank=True, verbose_name="")

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
