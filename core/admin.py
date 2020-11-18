from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(User)
