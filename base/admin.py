from django.contrib import admin
from .models import *

# Register your models here.
#master , keypass

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['name', 'question', 'answer_type', 'user', 'created', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'survey', 'submitted']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['name']
