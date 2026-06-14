from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('book/<int:pk>/', views.create_booking, name='create_booking'),
    path('dashboard/', views.booking_dashboard, name='booking_dashboard'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
