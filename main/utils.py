from datetime import datetime
from django.utils import timezone

from main.models import Likes
from users.models import User
import logging

logger = logging.getLogger(__name__)


def record_like(user_id, liked_user_id):
    try:
        user = User.objects.get(id=user_id)
        liked_user = User.objects.get(id=liked_user_id)

        if user != liked_user:
            like, created = Likes.objects.get_or_create(user=user, liked_user=liked_user,
                                                        defaults={'created_at': timezone.now()})
            if created:
                print(user, liked_user)
                logger.info('Like recorded: %s', like)
                like.save()
        else:
            print('User and liked_user should be different.')

    except User.DoesNotExist:
        print('User not found.')
    except Exception as e:
        print('Error recording like:', e)

