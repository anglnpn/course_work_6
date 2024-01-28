from django.contrib import admin

from mailing.models import Client, Partner, ClientsList, Mailing, Message, LogMailing

admin.site.register(Client)

admin.site.register(ClientsList)

admin.site.register(Mailing)

admin.site.register(Message)

admin.site.register(LogMailing)


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name_company', 'address', 'phone', 'email_company')
    search_fields = ('title', 'content',)
