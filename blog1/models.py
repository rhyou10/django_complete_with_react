from tkinter import CASCADE
from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+') #instagram post 와 똑같아서 related_name 포기시킴
    #author는 나중에 추가한 필수필드임, null=blank=false 이기 떄문이다.
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
