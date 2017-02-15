from django.contrib import admin

from tokenauth.models import Token


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'user', 'date_created')
    list_display_links = ('uuid', )
