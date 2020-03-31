from django.shortcuts import render
from django.views import generic
from about import models


# Create your views here.
class WebDesigning(generic.ListView):
    context_object_name = 'web_designing'
    queryset = models.WebDesigning.objects.all()
    template_name = 'webdev.html'


class SoftwareDevelopment(generic.ListView):
    context_object_name = 'software_development'
    queryset = models.WebDesigning.objects.all()
    template_name = 'software.html'


class MachineLearning(generic.ListView):
    context_object_name = 'machine_learning'
    queryset = models.WebDesigning.objects.all()
    template_name = 'ml.html'
