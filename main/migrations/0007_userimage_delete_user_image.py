# Generated by Django 4.2.1 on 2023-06-19 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='описание')),
                ('image', models.ImageField(upload_to='%Y/%m/%d', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Картинка для пользователей',
                'verbose_name_plural': 'Картинки для пользователей',
            },
        ),
        migrations.DeleteModel(
            name='User_image',
        ),
    ]
