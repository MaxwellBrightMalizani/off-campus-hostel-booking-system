from django.contrib import admin
from .models import Listing, Booking


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'address', 'created_at')
    search_fields = ('title', 'address')
    list_filter = ('created_at',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('student', 'listing', 'status', 'check_in_date', 'check_out_date', 'created_at')
    search_fields = ('student__username', 'listing__title')
    list_filter = ('status', 'created_at', 'check_in_date')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Student & Listing', {
            'fields': ('student', 'listing')
        }),
        ('Booking Details', {
            'fields': ('check_in_date', 'check_out_date', 'number_of_rooms', 'notes')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
