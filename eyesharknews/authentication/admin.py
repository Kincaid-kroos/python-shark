from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User,Profile

class UserAdmin(admin.ModelAdmin):
   list_display = ['username', 'email']


class ProfileAdmin(admin.ModelAdmin):
   list_display = ['user', 'full_name', 'verified']
   list_editable = ['verified']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)