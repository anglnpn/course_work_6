from django.urls import path
from mailing.views import PartnerCreateView, ClientsListCreateView, mailing_panel, MailingCreateView

app_name = 'mailing'

urlpatterns = [
    path('partner_registration/', PartnerCreateView.as_view(template_name='mailing/partner_registration.html'),
         name='partner_registration'),
    path('client_list_create/', ClientsListCreateView.as_view(), name='client_list_create'),
    path('mailing_management/', mailing_panel, name='mailing_panel'),
    path('mailing_form/', MailingCreateView.as_view(), name='mailing_form'),
]
