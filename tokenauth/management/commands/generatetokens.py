from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from tokenauth.models import Token


if hasattr(settings, 'USER_AUTH_MODEL'):
    User = settings.USER_AUTH_MODEL


class GenerateTokensCommand(BaseCommand):
    def handle(self, *args, **kwargs):

        users = User.objects.all()

        Token.objects.all().delete()

        for user in users:
            Token.objects.create(user=user)
