from django.shortcuts import render
from django.views import generic
from website import models


# Create your views here.
class WebDesigning(generic.ListView):
    context_object_name = 'web_designing'
    queryset = models.WebDesigning.objects.all()
    template_name = 'about/webdev.html'


class SoftwareDevelopment(generic.ListView):
    context_object_name = 'software_development'
    queryset = models.SoftwareDevelopment.objects.all()
    template_name = 'about/software.html'


class MachineLearning(generic.ListView):
    context_object_name = 'machine_learning'
    queryset = models.MachineLearning.objects.all().order_by('pk')
    template_name = 'about/ml.html'


class Skills(generic.ListView):
    context_object_name = 'skills'
    queryset = models.Skill.objects.all().order_by('-percentage')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Skills, self).get_context_data()

        context['workexperience'] = models.Experience.objects.all()

        return context
