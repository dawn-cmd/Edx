from project4.settings import TIME_ZONE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
from django.utils import timezone


class User(AbstractUser):
    followed = models.ManyToManyField("User", related_name="follower")
    likes = models.ManyToManyField("Post", related_name="liker")

class Post(models.Model):
    content = models.CharField(max_length=9999)
    poster = models.ForeignKey(User, related_name="post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField("Create time", default=timezone.now)

    def serialize(self):
        return {
            "content": self.content,
            "poster": self.poster.username,
            "timestamp": self.timestamp,
            "id": self.id,
        }