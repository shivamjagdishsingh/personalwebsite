from django.db import models


class Experience(models.Model):
    company_name = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)
    details = models.CharField(max_length=50, blank=True)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.company_name
