from about import views
from django.urls import path
from django.views.generic import TemplateView

app_name = 'about'
urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('webdesigning', views.WebDesigning.as_view(), name='webdesigning'),
    path('softwaredevelopment', views.SoftwareDevelopment.as_view(), name='softwaredevelopment'),
    path('machinelearning', views.MachineLearning.as_view(), name='machinelearning'),

]
