from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_LENGTH = 255


class CustomUser(AbstractUser):
    is_musician = models.BooleanField(default=False)
    is_blogger = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Blogger(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='blogger')
    subscriber_count = models.PositiveIntegerField(verbose_name='Количество подписчиков', default=0)
    completed_order_count = models.PositiveIntegerField(verbose_name='Количество выполненных заказов', default=0)
    tiktok_link = models.URLField(verbose_name='Ссылка на tiktok', blank=True, null=False)
    youtube_link = models.URLField(verbose_name='Ссылка на youtube', blank=True, null=False)
    rating = models.FloatField(verbose_name='Рейтинг', default=0.0)

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'Blogger {self.user.username=}'


class Musician(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name='Musician')

    USERNAME_FIELD = 'user'

    def __str__(self):
        return f'Musician {self.user.username=}'
