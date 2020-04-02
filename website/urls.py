from website import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'website'
urlpatterns = [
    path('', views.Skills.as_view(), name='index'),
    path('webdesigning', views.WebDesigning.as_view(), name='webdesigning'),
    path('softwaredevelopment', views.SoftwareDevelopment.as_view(), name='softwaredevelopment'),
    path('machinelearning', views.MachineLearning.as_view(), name='machinelearning'),

]
