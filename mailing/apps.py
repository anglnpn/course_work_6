from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        import mailing.signals

        # для рассылки
        from mailing.jobs import jobs
        sleep(2)
        jobs.start()
