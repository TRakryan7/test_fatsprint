from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', include('app.urls')),
]