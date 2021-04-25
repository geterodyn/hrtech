# Generated by Django 3.0.3 on 2020-03-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20200306_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='selected_choice',
        ),
        migrations.AddField(
            model_name='result',
            name='selected_choice',
            field=models.ManyToManyField(related_name='result_choices', to='polls.Choice'),
        ),
    ]
