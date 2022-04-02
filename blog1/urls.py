from . import views
from django.urls import path

app_name = "blog1"  #안넣어도 구동가능, URL_REVERSE에서 namespace 역할을 하게된다.

urlpatterns = [
    path('', views.PostList, name='post_list'),
]