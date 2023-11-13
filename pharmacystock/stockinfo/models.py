from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Pharmacy(models.Model):
    address = models.CharField(max_length=255, verbose_name='Адрес аптеки')
    number = models.IntegerField(verbose_name='Номер аптеки')
    metro_station = models.CharField(max_length=255, verbose_name='Ближайшее метро')

    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name_plural = 'Аптеки'
        verbose_name = 'Аптека'
        ordering = ['address']
    

class Medicine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название лекарства')
    dosage = models.CharField(max_length=255, verbose_name='Дозировка')
    quantity = models.IntegerField(verbose_name='Количество')
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    prescription_required = models.CharField(max_length=255, verbose_name='Условия отпуска')
    category = models.CharField(max_length=255, verbose_name='Категория')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Лекарства'
        verbose_name = 'Лекарство'
        ordering = ['name']

class Stock(models.Model):
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, verbose_name='Аптека')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Лекарство')
    quantity = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f"{self.medicine} at {self.pharmacy}"
    
    class Meta:
        verbose_name_plural = 'Запасы'
        verbose_name = 'Запас'
        ordering = ['-quantity']

