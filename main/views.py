from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from main.models import Questionnaire
from main.forms import QuestionnaireForm


class QuestionnaireCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Класс для создания анкеты
    """
    model = Questionnaire
    form_class = QuestionnaireForm
    success_url = reverse_lazy('main:main')
    template_name = 'main/new_questionnaire.html'
    permission_required = 'main.add_questionnaire'

    def __init__(self):
        self.request = None
        self.object = None

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)


class QuestionnaireListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Класс для создания списка анкет
    """
    model = Questionnaire
    template_name = 'main/index.html'
    permission_required = 'main.view_questionnaire'

    def get_queryset(self):
        queryset = super().get_queryset()

        for questionnaire in queryset:
            questionnaire.can_edit = questionnaire.author == self.request.user

        return queryset


class QuestionnaireDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    Класс для отображения анкеты
    """

    model = Questionnaire
    template_name = 'main/profile_view.html'
    permission_required = 'main.view_questionnaire'


class QuestionnaireUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
     Класс для обновления анкеты
     """

    model = Questionnaire
    form_class = QuestionnaireForm
    success_url = reverse_lazy('main:main')
    template_name = 'main/questionnaire_update.html'
    permission_required = 'main.change_questionnaire'


class QuestionnaireDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Класс для удаления анкеты
    """

    model = Questionnaire
    template_name = 'main/questionnaire_delete.html'
    permission_required = 'main.delete_questionnaire'
    success_url = reverse_lazy('main:main')
