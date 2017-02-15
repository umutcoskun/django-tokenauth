from django.apps import AppConfig


class TokenauthConfig(AppConfig):
    name = 'tokenauth'

    def ready(self):
        import tokenauth.signals
