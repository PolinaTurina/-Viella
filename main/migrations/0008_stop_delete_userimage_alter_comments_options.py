# Generated by Django 4.2.1 on 2023-06-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_userimage_delete_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('name_massage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.massage', verbose_name='противопоказание к:')),
                ('text', models.CharField(max_length=500, verbose_name='Список противопоказаний:')),
            ],
        ),
        migrations.DeleteModel(
            name='Userimage',
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-id'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
    ]
