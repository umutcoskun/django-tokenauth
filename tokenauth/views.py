from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import View

from tokenauth.auth import login

class Login(View):
    def get(self, request):
        login(request)

        next = request.GET.get('next', None)

        if next:
            return redirect(next)
        else:
            return redirect(settings.LOGIN_REDIRECT_URL)
