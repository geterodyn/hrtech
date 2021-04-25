from django.contrib import admin
from .models import Question, Choice, Polling
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'q_type')
    list_filter = ['q_type']
    search_fields = ['text']
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('Параметры вопроса', {'fields': ['q_type', 'image', 'duration'], 'classes': ['collapse']}), 
        ]
    inlines = [ChoiceInline]

class PollingAdmin(admin.ModelAdmin):
    fields = ('name', 'owners', 'pub_date', 'duration', 'slug', 'questions',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Polling, PollingAdmin)