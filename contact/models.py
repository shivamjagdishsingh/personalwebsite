from django.db import models


class PersonalDetails(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    about = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
