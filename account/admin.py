from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')

admin.site.register(UserProfile, UserProfileAdmin)
