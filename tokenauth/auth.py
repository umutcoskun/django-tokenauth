from uuid import UUID

from django.conf import settings
from django.contrib.auth import login as auth_login

from tokenauth.models import Token


def login(request, silence=False):
    param_name = 'token'

    if hasattr(settings, 'TOKENAUTH_PARAMETER_NAME'):
        param_name = settings.TOKENAUTH_PARAMETER_NAME

    hex = request.GET.get(param_name, None)

    if hex:
        try:
            # Ensure uuid4 format.
            value = UUID(hex, version=4)
        except ValueError:
            raise ValueError('Invalid token format.')

        try:
            token = Token.objects.get(uuid=value.hex)

            ALLOW_ADMINS = False
            if hasattr(settings, 'TOKENAUTH_ALLOW_ADMINS'):
                ALLOW_ADMINS = settings.TOKENAUTH_ALLOW_ADMINS

            if not ALLOW_ADMINS\
               and token.user.is_superuser:
                raise Exception('Super users cannot login via token.')

            auth_login(request, token.user)
        except Token.DoesNotExist:
            raise ValueError('The token does not exists.')
    elif not silence:
        raise ValueError('You should provide a token.')
