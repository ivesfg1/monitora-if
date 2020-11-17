from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'registration_type')


admin.site.register(User)
