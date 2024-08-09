from django.contrib import admin
from .models import Institution

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'is_certified', 'created_at', 'updated_at')
    list_filter = ('is_certified', 'created_at')
    search_fields = ('name', 'owner__username')
    ordering = ('name',)
    fieldsets = (
        (None, {'fields': ('name', 'description', 'owner', 'is_certified')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
    readonly_fields = ('created_at', 'updated_at')
