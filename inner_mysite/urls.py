# inner_mysite/urls.py
from django.urls import path

from inner_mysite.views import index

urlpatterns = [
    path('', index)
]