from django.contrib import admin
from .models import Table
# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'status')


admin.site.register(Table, TableAdmin)
