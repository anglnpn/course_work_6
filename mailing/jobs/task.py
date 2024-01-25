import pytz
from django.conf import settings
from datetime import datetime

from django.core.mail import send_mail

from mailing.models import Mailing


def send_mailing():
    """
    Функция отвечает за рассылку сообщений пользователям
    :return: временной период для crontab
    """
    global client_email, theme, text, periodicity

    # определение текущего времени
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    # создание объекта с применением фильтра
    mailings = Mailing.objects.filter(date__lte=current_datetime).filter(status='создана')

    for mailing in mailings:
        # получение временного периода
        periodicity = mailing.periodicity

        # получение списка клиентов для рассылки
        clients_lists = mailing.clients_list.all()

        for clients_list in clients_lists:

            # Получение клиентов из списка
            clients = clients_list.clients.all()

            for client in clients:
                # получение email клиента
                client_email = client.email

        # получение темы и текста сообщения для рассылки
        message = mailing.message if hasattr(mailing, 'message') else None
        text = message.text
        theme = message.theme

    # сбор сообщения
    send_mail(
        subject=theme,
        message=text,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[client_email]
    )

    return periodicity
