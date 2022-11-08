from django.db import models

from account_service.models import CustomUser


# Create your models here.
class Offer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='offers')
    price = models.PositiveIntegerField(verbose_name='Цена')
