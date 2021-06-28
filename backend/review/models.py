from django.db import models
from django.contrib.auth import get_user_model

from restaurant.models import Restaurant

User = get_user_model()


def user_directory_path(instance, filename):
    return f'{instance.author}/{filename}'


class Review(models.Model):
    content = models.TextField(max_length=1000, blank=False)
    rating = models.CharField(max_length=5, choices=[('1', 'terrible'), ('2', 'bad'), ('3', 'average'),
                                                     ('4', 'good'), ('5', 'excellent')])
    images = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(to=User, on_delete=models.CASCADE, blank=False)
    restaurant = models.OneToOneField(to=Restaurant, on_delete=models.CASCADE, blank=False,
                                      related_name='review')

    def __str__(self):
        return f'Review #{self.id} from {self.author}'
