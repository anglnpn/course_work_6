from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


from mailing.forms import PartnerForm, ClientsListForm, MailingForm, MessageForm
from mailing.models import Partner, ClientsList, Mailing


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
    Модель для создания списка клиентов
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
    Модель для создания рассылки и сообщения
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
