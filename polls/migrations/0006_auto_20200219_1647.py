# Generated by Django 3.0.3 on 2020-02-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20200219_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
