from django.contrib import admin

from main.models import Questionnaire


# Register your models here.


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'age', 'sex', 'city', 'description')
    search_fields = ('name', 'surname', 'age', 'sex', 'city', 'description')

