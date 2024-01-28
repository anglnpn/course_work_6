from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from mailing.models import Client, Partner
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    """
    Сигнал для автоматического создания клиента при регистрации пользователя
    Исключен персонал сайта и не активных пользователей
    """
    if created and not instance.is_staff and instance.is_active:
        # При создании нового пользователя создаем соответствующего клиента
        Client.objects.create(
            client=instance,
            name=instance.name,
            surname=instance.surname,
            email=instance.email

        )


@receiver(post_save, sender=Partner)
def create_partner(sender, instance, created, **kwargs):
    """
    Сигнал для обработки создания партнера
    """

    group_name = 'partner_user'
    user_group, created_ = Group.objects.get_or_create(name=group_name)

    # Проверяем, создан ли объект
    if created:
        # Добавляем пользователя в группу "partner_user"
        instance.user.groups.add(user_group)

        # Удаляем связанный клиент, если он существует
        client = Client.objects.filter(client=instance.user).first()
        if client:
            client.delete()
