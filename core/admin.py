from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('subjects',)


admin.site.register(User, UserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Request)
