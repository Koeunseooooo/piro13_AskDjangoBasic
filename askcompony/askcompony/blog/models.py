from django.db import models
from django.conf import settings
from askcompony.utils import uuid_upload_to

# Create your models here.

class Post(models.Model):
    author_name=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    content=models.TextField()
    photo = models.ImageField(upload_to=uuid_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    message = models.TextField()

