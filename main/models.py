from django.db import models

from config.settings import TIPOLOGIA_CHOICES
from users.models import User

from utils import NULLABLE


class Questionnaire(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст')
    sex = models.CharField(max_length=50, verbose_name='пол', choices=TIPOLOGIA_CHOICES)
    city = models.CharField(max_length=50, verbose_name='город')
    description = models.CharField(max_length=500, verbose_name='описание')
    image = models.ImageField(upload_to='media/', verbose_name='изображение', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='автор', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'анкета'
