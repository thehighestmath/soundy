from django.db import models

from account_service.models import Blogger


class Offer(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='offers')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Короткое описание')
