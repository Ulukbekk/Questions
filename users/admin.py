from django.contrib import admin

from users.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'email',
                    'total')
