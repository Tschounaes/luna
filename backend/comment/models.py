from django.db import models
from restaurant.models import Restaurant
from review.models import Review
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(to=User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE, blank=False)
    liked_by = models.ManyToManyField(to=User, related_name='likes')

    def __str__(self):
        return f'Comment #{self.id}, authored by {self.author} on {self.review}'
