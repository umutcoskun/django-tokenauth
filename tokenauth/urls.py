from django.conf.urls import url

from tokenauth.views import Login

urlpatterns = [
    url(r'^login$', Login.as_view(), name='login'),
]
