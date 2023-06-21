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
        ordering = ["id"]
        verbose_name = 'Массаж'
        verbose_name_plural = 'Массажи'

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=32, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание")
    price = models.CharField(max_length=32, verbose_name='Цена')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Доп услуга'
        verbose_name_plural = 'Доп услуги'

    def __str__(self):
        return self.name
    

class Sertificats(models.Model):
    view = models.CharField(max_length=32, verbose_name="Вид сертификата")
    description = models.TextField(verbose_name="Описание")
    price = models.CharField(max_length=5, verbose_name='Цена')

    class Meta:
        ordering = ["id"]
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.view


class Banks(models.Model):
    name = models.CharField(max_length=32, verbose_name='банк')

    class Meta:
        ordering = ["name"]
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

    def __str__(self):
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=32,verbose_name='Ваше имя:')
    text = models.TextField(blank=False,verbose_name='Текст отзыва:')
    create_date = models.DateTimeField(auto_now=True,verbose_name='Дата')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)

    class Meta():
        ordering = ["-id"]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (self.text[:20] +"...")


    

class Stop(models.Model):
    name_massage = models.OneToOneField(Massage, on_delete = models.CASCADE, primary_key = True, verbose_name='противопоказание к:')
    text = models.TextField(max_length=800 ,verbose_name='Список противопоказаний:')

    def __str__(self):
        return self.name_massage