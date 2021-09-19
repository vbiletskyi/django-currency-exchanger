from django.db import models


class Exchanger(models.Model):
    rate = models.FloatField(verbose_name='Курс валюты')
    created_date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return str(self.rate)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

