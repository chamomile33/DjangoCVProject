from django.contrib import admin
from django.contrib.auth import get_user_model
from users.models import CSVModel
from django.contrib.auth.admin import UserAdmin

User = get_user_model()
admin.site.register(CSVModel)

@admin.register(User)
class UserAdmin(UserAdmin):
    pass
