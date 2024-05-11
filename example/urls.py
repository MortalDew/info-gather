# example/urls.py
from django.urls import path

from example.views import index, update_data


urlpatterns = [
    path('', index),
    path('cron/', cron.cron.update_data(), name='cron'),
]