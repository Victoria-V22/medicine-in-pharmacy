from django.urls import path
from stockinfo.views import *

urlpatterns = [
    path('', index),
]
