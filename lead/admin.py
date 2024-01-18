from django.contrib import admin
from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'status', 'priority', 'created_by', 'created_at', 'updated_at')
    search_fields = ('name', 'company')
    list_filter = ('status', 'priority', 'created_by', 'created_at', 'updated_at')

admin.site.register(Lead, LeadAdmin)
