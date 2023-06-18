# Generated by Django 4.2.1 on 2023-06-18 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_banks_alter_massage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название услуги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(max_length=32, verbose_name='Цена')),
            ],
        ),
    ]
