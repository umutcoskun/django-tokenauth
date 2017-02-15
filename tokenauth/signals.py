from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from tokenauth.models import Token


if hasattr(settings, 'USER_AUTH_MODEL'):
    user = settings.user_auth_model


def create_user_token(sender, instance, created, **kwargs):
    if created:
        token = Token(user=instance)
        token.save()

post_save.connect(create_user_token, sender=User)

