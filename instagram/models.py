from email import message
from django.db import models

class Post(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=rue)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
