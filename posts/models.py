from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True, related_name="liked_posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def toggle_like(self, user):
        #  liked
        if user in self.liked.all():
            self.liked.remove(user)
        # not liked
        else:
            self.liked.add(user)
