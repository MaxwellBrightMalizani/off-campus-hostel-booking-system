from django.contrib import admin
from .models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'address', 'created_at')
    search_fields = ('title', 'address')
    list_filter = ('created_at',)
