from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import TIPOLOGIA_CHOICES
from utils import NULLABLE


class User(AbstractUser):
    """
    Модель для создания пользователя.
    Создается при регистрации.
    """
    username = None
    name = models.CharField(max_length=50, verbose_name='имя')
    surname = models.CharField(max_length=50, verbose_name='фамилия')
    age = models.IntegerField(verbose_name='возраст', **NULLABLE)
    sex = models.CharField(max_length=50, verbose_name='пол', choices=TIPOLOGIA_CHOICES)
    description = models.CharField(max_length=500, verbose_name='описание', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='media/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=50, verbose_name='город', **NULLABLE)
    verification_code = models.CharField(max_length=50, verbose_name='код верификации email', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'пользователь'
