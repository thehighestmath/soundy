from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_LENGTH = 255


class Search(models.Model):
    class Categories(models.TextChoices):
        ANY = 'any', _('Любая')
        SPORT = 'sport', _('Спорт')
        ART = 'art', _('Рисование')

    class SubscriberCount(models.TextChoices):
        FROM_0_TO_1000 = '0-1000', _('От 0 до 1000')
        FROM_1000_TO_2000 = '1000-2000', _('От 1000 до 2000')

    class Result(models.TextChoices):
        ANY = 'any', _('Любой')

    class LastActivity(models.TextChoices):
        RECENTLY = 'recently', _('Недавно')

    class Rating(models.TextChoices):
        FROM_0_TO_1000 = '0-1000', _('От 0 до 1000')
        FROM_1000_TO_2000 = '1000-2000', _('От 1000 до 2000')

    category = models.CharField(
        verbose_name='Категория',
        max_length=MAX_LENGTH,
        choices=Categories.choices,
        default=Categories.ANY,
    )
    subscriber_count = models.CharField(
        verbose_name='Количество подписчиков',
        max_length=MAX_LENGTH,
        choices=SubscriberCount.choices,
        default=SubscriberCount.FROM_0_TO_1000,
    )
    last_activity = models.CharField(
        verbose_name='Последняя активность',
        max_length=MAX_LENGTH,
        choices=LastActivity.choices,
        default=LastActivity.RECENTLY,
    )
    result = models.CharField(
        verbose_name='Результат',
        max_length=MAX_LENGTH,
        choices=Result.choices,
        default=Result.ANY,
    )
    rating = models.CharField(
        verbose_name='Рейтинг',
        max_length=MAX_LENGTH,
        choices=Rating.choices,
        default=Rating.FROM_0_TO_1000,
    )

    def __str__(self):
        return f'Search: {self.__dir__()}'
