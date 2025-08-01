from django.contrib import admin
from .models import Vegetable

admin.site.register(Vegetable)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','phone_number','address']
