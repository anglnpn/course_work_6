
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from mailing.forms import PartnerForm, ClientsListForm, MailingForm, MessageForm
from mailing.models import Partner, ClientsList, Mailing, LogMailing


class PartnerCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для создания блоговой записи
    """
    model = Partner
    form_class = PartnerForm
    template_name = 'mailing/partner_registration.html'
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        # Устанавливаем пользователя и partner_id перед сохранением Partner
        form.instance.user = self.request.user
        form.instance.partner_id = self.request.user.id
        return super().form_valid(form)


class ClientsListCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания списка клиентов
    """
    model = ClientsList
    form_class = ClientsListForm
    template_name = 'mailing/client_list_create.html'
    success_url = reverse_lazy('mailing:mailing_panel')

    def form_valid(self, form):
        partner = self.request.user.partner
        form.instance.partner = partner
        response = super().form_valid(form)
        return response


class MailingCreateView(LoginRequiredMixin, CreateView):
    """
    Контроллер для создания рассылки и сообщения
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_form.html'
    success_url = reverse_lazy('mailing:mailing_panel')

    def form_valid(self, form):
        partner = self.request.user.partner
        form.instance.partner = partner
        response = super().form_valid(form)

        message_form = MessageForm(self.request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.mailing = self.object
            message.save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message_form'] = MessageForm()
        return context


def mailing_panel(request):
    """
   Вывод страницы с управлением рассылкой
    """
    return render(request, 'mailing/mailing_management.html')


def mailings_manage(request):
    """
   Вывод страницы с управлением рассылкой
    """
    return render(request, 'mailing/manage_mailing.html')


class PartnerListView(LoginRequiredMixin, ListView):
    """
    Контроллер для создания списка пользователей сервиса
    """
    model = Partner
    form_class = PartnerForm
    template_name = 'mailing/partners_list_manage.html'


class MailingListView(LoginRequiredMixin, ListView):
    """
    Контроллер для создания списка рассылок для менеджера
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailings_list_manage.html'


class MailingDetailView(LoginRequiredMixin, DetailView):
    """
    Контроллер для просмотра рассылки для менеджера
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_detail_manage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.object.message
        return context


@login_required
def toggle_block_status(request, mailing_id):
    """
   Функция для переключения статуса активности рассылки
    """
    mailing = get_object_or_404(Mailing, id=mailing_id)

    # Переключаем статус блокировки
    if request.user.has_perm('mailing.can_blocked'):
        mailing.is_active = not mailing.is_active
        mailing.save()
        return redirect('mailing:mailings_list_manage')
    else:
        # Обработка случая, когда у пользователя нет нужных прав
        return render(request, 'main/403.html')


@login_required
def toggle_block_partners(request, partner_id):
    """
   Функция для переключения статуса активности у партнера
    """
    partners = get_object_or_404(Partner, id=partner_id)

    # Переключаем статус блокировки
    if request.user.has_perm('mailing.can_blocked'):
        partners.is_active = not partners.is_active
        partners.save()
        return redirect('mailing:partners_list_manage')
    else:
        # Обработка случая, когда у пользователя нет нужных прав
        return render(request, 'main/403.html')


def custom_permission_denied(request, exception):
    """
    При ошибке перевод на собственную страницу
    """
    return render(request, 'main/403.html', status=403)


class MailingPartnersListView(LoginRequiredMixin, ListView):
    """
     Класс для создания списка рассылок для менеджера
     """
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailings_list_user.html'

    def get_queryset(self):
        # Фильтрация рассылок по текущему пользователю
        return Mailing.objects.filter(partner__partner=self.request.user)


class MailingPartnersDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для просмотра рассылки для менеджера
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_detail_user.html'

    def get_queryset(self):
        # Фильтрация рассылок по текущему пользователю
        return Mailing.objects.filter(partner__partner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = self.object.message

        # Получение статистики из логов рассылки
        logs_fail = LogMailing.objects.filter(mailing=self.object).filter(status='неудачно')
        logs_good = LogMailing.objects.filter(mailing=self.object).filter(status='успешно').count
        context['logs_fail'] = logs_fail
        context['logs_good'] = logs_good
        return context


class MailingPartnersUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс для просмотра рассылки для менеджера
    """
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing/mailing_update_user.html'
    success_url = reverse_lazy('mailing:mailings_list_user')


class MailingPartnersDeleteView(LoginRequiredMixin, DeleteView):
    """
    Контроллер для показа рассылок партнеру
    """

    model = Mailing
    success_url = reverse_lazy('mailing:mailings_list_user')
    template_name = 'mailing/mailing_confirm_delete.html'


class PartnersDetailView(LoginRequiredMixin, DetailView):
    """
    Класс для просмотра рассылки для менеджера
    """
    model = Partner
    form_class = PartnerForm
    template_name = 'mailing/partners_detail_manage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


