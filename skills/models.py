from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=50, blank=True)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name
