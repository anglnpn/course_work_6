from django import forms
from mailing.models import Partner, Client, ClientsList, Mailing, Message


class PartnerForm(forms.ModelForm):
    """
    Форма для валидации и стилизации партнера
    """

    class Meta:
        model = Partner
        fields = ['name_company', 'address', 'phone', 'email_company']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(forms.ModelForm):
    """
    Форма для валидации и стилизации клиента
    """

    class Meta:
        model = Client
        fields = ['name', 'surname', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientsListForm(forms.ModelForm):
    """
    Форма для списка клиентов для партнера
    """

    class Meta:
        model = ClientsList
        fields = ['name', 'clients']

    # форма для добавления клиента в список
    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class MailingForm(forms.ModelForm):
    """
    Форма для рассылки
    """

    class Meta:
        model = Mailing
        fields = ['name_mailing', 'clients_list', 'periodicity']

    # форма для добавления списка клиентов
    clients_list = forms.ModelMultipleChoiceField(
        queryset=ClientsList.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class MessageForm(forms.ModelForm):
    """
    Форма для сообщения
    """

    class Meta:
        model = Message
        fields = ['theme', 'text']



