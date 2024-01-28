from django.urls import path
from mailing.views import PartnerCreateView, ClientsListCreateView, mailing_panel, MailingCreateView, mailings_manage, \
    PartnerListView, MailingListView, MailingDetailView, toggle_block_status, MailingPartnersListView, \
    MailingPartnersDetailView, MailingPartnersUpdateView, MailingPartnersDeleteView, PartnersDetailView, \
    toggle_block_partners

app_name = 'mailing'

urlpatterns = [
    path('partner_registration/', PartnerCreateView.as_view(template_name='mailing/partner_registration.html'),
         name='partner_registration'),
    path('client_list_create/', ClientsListCreateView.as_view(), name='client_list_create'),
    path('mailing_management/', mailing_panel, name='mailing_panel'),
    path('mailing_form/', MailingCreateView.as_view(), name='mailing_form'),
    path('manage_mailing/', mailings_manage, name='mailings_manage'),
    path('partners_list_manage/', PartnerListView.as_view(), name='partners_list_manage'),
    path('mailings_list_manage/', MailingListView.as_view(), name='mailings_list_manage'),
    path('mailing_detail_manage/<int:pk>/', MailingDetailView.as_view(), name='mailing_detail_manage'),
    path('toggle_block_status/<int:mailing_id>/', toggle_block_status, name='toggle_block_status'),
    path('mailings_list_user/', MailingPartnersListView.as_view(), name='mailings_list_user'),
    path('mailing_detail_user/<int:pk>/', MailingPartnersDetailView.as_view(), name='mailing_detail_user'),
    path('mailing_update_user/<int:pk>/', MailingPartnersUpdateView.as_view(), name='mailing_update_user'),
    path('mailing_confirm_delete/<int:pk>/', MailingPartnersDeleteView.as_view(), name='mailing_confirm_delete'),
    path('partners_detail_manage/<int:pk>/', PartnersDetailView.as_view(), name='partners_detail_manage'),
    path('toggle_block_partners/<int:partner_id>/', toggle_block_partners, name='toggle_block_partners'),

]
