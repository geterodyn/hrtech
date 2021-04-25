from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta



class Question(models.Model):
    """Вопросы опросов"""
    QUESTION_TYPES = (
        ('single', 'Один ответ'), ('multiple', 'Несколько ответов')
    )
    text = models.TextField('Вопрос')
    image = models.ImageField('Изображение', null=True, blank=True, upload_to='images/')
    duration = models.DurationField(
        'Время на вопрос',
        null=True,
        blank=True,
        help_text='формат `[ДД] [[чч:]мм:]сс`'
        )
    q_type = models.CharField('Тип вопроса', max_length=20, choices=QUESTION_TYPES, default='single')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Polling(models.Model):
    """Опросники"""
    owners = models.ManyToManyField(User, related_name='pollings')
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Дата публикации опроса', default=timezone.now)
    duration = models.DurationField(
        'Время на опрос',
        null=True,
        blank=True,
        help_text='формат `[ДД] [[чч:]мм:]сс`'
        )
    slug = models.SlugField(max_length=100)
    questions = models.ManyToManyField(Question, related_name='polling_questions')

    class Meta:
        verbose_name = 'Опросник'
        verbose_name_plural = 'Опросники'

    def __str__(self):
        return self.name

class Choice(models.Model):
    """Варианты ответов"""
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
        )
    text = models.CharField('', max_length=250)
    score = models.IntegerField('Баллы', default=0)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return self.text

class Result(models.Model):
    """Результаты опроса"""
    owner = models.ForeignKey(User, related_name='results', on_delete=models.CASCADE)
    polling = models.ForeignKey(Polling, related_name='results', on_delete=models.CASCADE)
    selected_choice = models.ManyToManyField(Choice, related_name='result_choices')

    def __str__(self):
        return f"Result for {self.owner} on poll {self.polling}"