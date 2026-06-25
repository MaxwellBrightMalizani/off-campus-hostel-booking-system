from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('book/<int:pk>/', views.create_booking, name='create_booking'),

    # Student booking
    path('dashboard/', views.booking_dashboard, name='booking_dashboard'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

    # Owner dashboard
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('owner/booking/<int:booking_id>/decide/', views.owner_booking_decide, name='owner_booking_decide'),

    # Owner properties (hostel details)
    path('owner/properties/', views.owner_property_list, name='owner_property_list'),
    path('owner/properties/new/', views.owner_property_create, name='owner_property_create'),
    path('owner/properties/<int:pk>/edit/', views.owner_property_update, name='owner_property_update'),
]

