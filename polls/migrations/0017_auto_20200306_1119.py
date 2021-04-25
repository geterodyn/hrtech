# Generated by Django 3.0.3 on 2020-03-06 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_auto_20200305_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='selected_choice',
        ),
        migrations.AddField(
            model_name='choice',
            name='selected',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Result'),
            preserve_default=False,
        ),
    ]