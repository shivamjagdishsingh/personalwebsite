from django.urls import include, path
from django.contrib import admin
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls', namespace='about')),
    # path('device/', include('device.urls', namespace='device')),


]