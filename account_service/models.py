from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_LENGTH = 255


class CustomUser(AbstractUser):
    tiktok_link = models.URLField(verbose_name='Ссылка на tiktok', blank=True, null=False)

    def __str__(self):
        return self.username
