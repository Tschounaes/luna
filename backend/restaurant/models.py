from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()


def user_directory_path(instance, filename):
    return f'{instance.name}/{filename}'


class Restaurant(models.Model):
    name = models.CharField(max_length=100, blank=False)
    category = models.JSONField(max_length=100, default=list)
    country = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=50)
    website = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "From 9 up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.CharField(max_length=100)
    hours = models.CharField(max_length=100)
    price_level = models.CharField(max_length=10, choices=[('1', '$'), ('2', '$$'), ('3', '$$$')],
                                   default='1')
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    owner = models.ForeignKey(to=User, blank=False, null=False, on_delete=models.CASCADE,
                              related_name='owner')

    def __str__(self):
        return f'restaurant {self.name}, owner {self.owner}'


