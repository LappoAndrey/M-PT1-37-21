from django.db import models
from catalog import models as catalog


class Dealer(models.Model):
    company_name = models.CharField(max_length=50, blank=False, verbose_name='Название')
    url = models.URLField(verbose_name='Сайт')
    phone = models.CharField(max_length=50, verbose_name='Номер телефона')
    city = models.CharField(max_length=50, blank=False, verbose_name='Город')
    address = models.CharField(max_length=50, blank=False, verbose_name='Адрес')
    coordinates = models.CharField(max_length=50, blank=False, verbose_name='Координаты в Яндекс.Картах')
    brand = models.ForeignKey(catalog.Brand, on_delete=models.CASCADE, verbose_name='Марка')

    def __str__(self):
        return self.company_name
