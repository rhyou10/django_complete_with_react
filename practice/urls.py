from django.urls import URLPattern
from django.urls import path

from . import views

urlpatterns=[
    path('', views.view_test, name='view_test'),
]