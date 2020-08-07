from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
