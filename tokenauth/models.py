import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


if hasattr(settings, 'USER_AUTH_MODEL'):
    user = settings.user_auth_model


class Token(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        default_related_name = 'token'

    def __str__(self):
        return '<Token {} {}>'.format(self.user.username, self.uuid)
