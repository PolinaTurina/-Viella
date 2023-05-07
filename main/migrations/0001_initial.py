# Generated by Django 4.2.1 on 2023-05-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название массажа')),
                ('description', models.TextField(verbose_name='Описание')),
                ('fifteen_minutes', models.CharField(max_length=32, verbose_name='Цена за 15 минут')),
                ('thirty_minutes', models.CharField(max_length=32, verbose_name='Цена за 30 минут')),
                ('forty_five_minutes', models.CharField(max_length=32, verbose_name='Цена за 45 минут')),
                ('sixty_minutes', models.CharField(max_length=32, verbose_name='Цена за 60 минут')),
                ('image', models.ImageField(upload_to='%Y/%m/%d', verbose_name='Изображение')),
            ],
        ),
    ]
