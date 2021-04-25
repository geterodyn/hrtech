import q
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from polls.models import Polling, Question, Choice,  Result


class PollingList(LoginRequiredMixin, ListView):
    """Выводит список опросов, доступных для пользователя"""
    model = Polling
    context_object_name = 'pollings'

    def get_queryset(self):
        user = self.request.user
        return user.pollings.all()

class PollingDetail(DetailView):
    """Детали по опросу по slug_field='slug' """
    model = Polling


class PollingExec(View):
    """Отображение и выполнение опроса"""
    def get(self, request, slug, *args, **kwargs):
        polling = Polling.objects.get(slug=slug)
        # q.d()
        pk = kwargs['pk']
        question = polling.questions.get(id=pk)
        question_index = sorted([q.id for q in polling.questions.all()]).index(question.id)
        return render(request, 'polls/polling_exec.html', {'question': question, 'question_num': question_index+1})

    def post(self, request, slug, *args, **kwargs):
        # q.d()
        pk = kwargs['pk']
        question = Question.objects.get(id=pk)
        user = request.user
        polling = Polling.objects.get(slug=slug)

        question_index = sorted([q.id for q in polling.questions.all()]).index(question.id)
        
        if Result.objects.filter(
            polling=polling,
            owner=user
            ).exists():
            result = Result.objects.filter(
            owner = user,
            polling = polling
            ).last()
        
        else:
            result = Result.objects.create(
                polling=polling,
                owner=user
            )
        if question_index == 0:
            result.selected_choice.clear()
        try:
            choice_ids = dict(request.POST)['choice']
            for choice_id in choice_ids:
                result.selected_choice.add(Choice.objects.get(id=choice_id))
        except KeyError:
            return render(request, 'polls/polling_exec.html',
            {'question': question, 'question_num': question_index+1, 'error_message': 'Не выбран вариант!'})
        try:
            next_id = sorted([q.id for q in polling.questions.all()])[question_index+1]
            Question.objects.get(id=next_id)
            return redirect(reverse('polls:execute', args=[slug, next_id]))
        except (Question.DoesNotExist, IndexError):
            return redirect(reverse('polls:result', args=[slug, result.id]))


class PollingResult(DetailView):
    """Результаты опроса """
    model = Result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        choices = self.object.selected_choice.all()
        question_ids = {c.question.id for c in choices}
        scores = [[c.score  for c in choices if c.question.id==i] for i in question_ids]
        total = sum([max(score)*int(all(score)) for score in scores])
        context['total'] = total
        return context
    