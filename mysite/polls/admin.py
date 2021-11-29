from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    '''adds choices to add question page'''

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)