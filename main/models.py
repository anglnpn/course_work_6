from django.db import models

from users.models import User


class Likes(models.Model):
    """
    Модель для записи лайка (кто лайкнул, кого лайкнул)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_given')
    liked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes_received')
    created_at = models.DateTimeField(auto_now_add=True)
