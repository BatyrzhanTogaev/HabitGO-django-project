from django.db import models
from django.contrib.auth.models import AbstractUser


class SubscriptionUser(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('vip', 'Vip'),
        ('premium', 'Premium'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        unique=True)

    def __str__(self):
        return self.get_status_display()


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    status = models.ForeignKey(
        SubscriptionUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='users'
        )
