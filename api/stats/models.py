from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class RawModel(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='raws',
        verbose_name='Автор'
    )

    name = models.CharField(
        'Сырье',
        max_length=200,
        null=False,
        blank=False
    )
    iron_con = models.FloatField(
        'Содержание железа',
        null=False,
        blank=False
    )
    silicon_con = models.FloatField(
        'Содержания кремния',
        null=False,
        blank=False
    )
    aluminum_con = models.FloatField(
        'Содержание алюминия',
        null=False,
        blank=False
    )
    calcium_con = models.FloatField(
        'Содержание кальция',
        null=False,
        blank=False
    )
    sulfure_con = models.FloatField(
        'Содержание серы',
        null=False,
        blank=False
    )
    month = models.CharField(
        'Месяц',
        choices=settings.MONTHES,
        max_length=10,
        null=False,
        blank=False
    )
