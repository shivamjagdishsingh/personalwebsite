from about import views
from django.urls import path

app_name = 'about'
urlpatterns = [
    path('webdesigning', views.WebDesigning.as_view(), name='webdesigning'),
    path('softwaredevelopment', views.SoftwareDevelopment.as_view(), name='softwaredevelopment'),
    path('machinelearning', views.MachineLearning.as_view(), name='machinelearning'),

]
