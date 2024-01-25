from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from .task import send_mailing

# получение временного периода
periodicity = send_mailing()


def start():
    scheduler = BackgroundScheduler()
    # запуск отправки рассылки с определенным периодом
    scheduler.add_job(send_mailing, trigger=CronTrigger.from_crontab(periodicity))
    scheduler.start()
