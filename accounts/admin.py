from django.contrib import admin
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone']