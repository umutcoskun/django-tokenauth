# django-tokenauth
Token based authentication for Django.

Creates unique tokens for each User that lets them authenticate via URL parameter. Tokens will be checked before the response creation so the user not need to refresh the page if the user is not authenticated already.

For example: `http://example.com/my-statistics?token=59070855-502f-44fa-b412-2ff256b864c7`

You can use tokens to create magic login links like Slack 

## Installation
Currently, only the development version is available. :)

```pip3 install git+git://github.com/umutcoskun/django-tokenauth.git```

Then you must `tokenauth` to your `INSTALLED_APPS` and and `tokenauth.middleware.LoginMiddleware` to your `MIDDLEWARE`. Middleware will make available token authentication for all URLs. If you dont want this, see `Common View` section.

## Usage

```
token, created = Token.objects.get_or_create(user=request.user)
```

You can bulk create tokens via management command:

```
./manage.py generatetokens
```

## Customization
You should define these settings in your main *settings.py* file. Otherwise, TokenAuth will use the default settings.

* `LOGIN_REDIRECT_URL` If you are using common view, authenticated users will be redirected to the URL.
* `USER_AUTH_MODEL` Authentication model for Users. (default: django.contrib.auth.models.User)
* `TOKENAUTH_PARAMETER_NAME` Name of the GET parameter that TokenAuth uses. (default: token)
* `TOKENAUTH_ALLOW_ADMINS` Can admins login via tokens? (default: False)

## Authentication via common View:
If you dont want to use LoginMiddleware, you can use LoginView. You should import TokenAuth's URL patterns to projects URLs.


```
urlpatterns = [
    # ...
    url(r'^tokenauth/', include('tokenauth.urls', namespace='tokenauth')),
]
```

For example: `http://example.com/tokenauth/login?token=59070855-502f-44fa-b412-2ff256b864c7`
