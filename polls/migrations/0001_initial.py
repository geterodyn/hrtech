# Generated by Django 3.0.3 on 2020-02-19 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Вопрос')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('question_duration', models.DurationField(null=True, verbose_name='Время на вопрос')),
                ('question_type', models.CharField(choices=[('single', 'Один ответ'), ('multiple', 'несколько ответов')], default='single', max_length=20, verbose_name='Тип вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='Polling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации опроса')),
                ('poll_duration', models.DurationField(null=True, verbose_name='Время на опрос')),
                ('slug', models.SlugField(max_length=100)),
                ('questions', models.ManyToManyField(to='polls.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=250)),
                ('score', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='polls.Question')),
            ],
        ),
    ]