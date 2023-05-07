from django.db import models


class Massage(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название массажа")
    description = models.TextField(verbose_name="Описание")
    fifteen_minutes = models.CharField(max_length=32, verbose_name='Цена за 15 минут')
    thirty_minutes = models.CharField(max_length=32, verbose_name='Цена за 30 минут')
    forty_five_minutes = models.CharField(max_length=32, verbose_name='Цена за 45 минут')
    sixty_minutes = models.CharField(max_length=32, verbose_name='Цена за 60 минут')
    image = models.ImageField(upload_to='%Y/%m/%d', verbose_name="Изображение")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массажи'

    def __str__(self):
        return self.name