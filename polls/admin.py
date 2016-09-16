from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently',)
    fields = ['pub_date', 'question_text', ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
