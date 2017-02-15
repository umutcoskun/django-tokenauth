# django-tokenauth
Token based authentication for Django.

Creates unique tokens for each User that lets them authenticate via URL parameter. Tokens will be checked before the response creation so the user not need to refresh the page if the user is not authenticated already.

For example: `http://example.com/my-statistics?token=59070855-502f-44fa-b412-2ff256b864c7`

## Installation
Currently, only the development version is available. :)

```pip3 install git+git://github.com/umutcoskun/django-tokenauth.git```

## Customization
You should define these settings in your main *settings.py* file. Otherwise, TokenAuth will use the default settings.

* `LOGIN_REDIRECT_URL` Authenticated users will be redirected to the URL.
* `USER_AUTH_MODEL` Authentication model for Users. (default: django.contrib.auth.models.User)
* `TOKENAUTH_PARAMETER_NAME` Name of the GET parameter that TokenAuth uses. (default: token)
* `TOKENAUTH_ALLOW_ADMINS` Can admins login via tokens? (default: False)
