from types import SimpleNamespace

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import Booking, Listing


DEFAULT_LISTINGS = [
    SimpleNamespace(
        id=1,
        pk=1,
        title='Cozy shared room near campus',
        description='A quiet room with study space, free Wi-Fi, and easy access to local shops.',
        price='150.00',
        address='123 College Lane, Near Campus',
    ),
    SimpleNamespace(
        id=2,
        pk=2,
        title='Affordable studio apartment',
        description='Private studio with kitchenette, shared laundry, and close bus service.',
        price='260.00',
        address='78 Offcampus Road, City Center',
    ),
]


def home(request):
    try:
        featured = list(Listing.objects.all()[:6])
        if not featured:
            featured = DEFAULT_LISTINGS[:6]
    except Exception:
        featured = DEFAULT_LISTINGS[:6]
    return render(request, 'home.html', {'featured': featured})


def listing_list(request):
    try:
        listings = list(Listing.objects.all())
        if not listings:
            listings = DEFAULT_LISTINGS
    except Exception:
        listings = DEFAULT_LISTINGS
    return render(request, 'listings/listing_list.html', {'listings': listings})


def listing_detail(request, pk):
    try:
        listing = get_object_or_404(Listing, pk=pk)
    except Exception:
        listing = next((item for item in DEFAULT_LISTINGS if item.id == pk), None)
        if listing is None:
            raise

    existing_booking = None
    if request.user.is_authenticated and isinstance(listing, Listing):
        existing_booking = Booking.objects.filter(
            user=request.user,
            listing=listing,
            status=Booking.STATUS_PENDING,
        ).first()

    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'existing_booking': existing_booking,
    })


@login_required
def create_booking(request, pk):
    if request.method != 'POST':
        return redirect('listings:listing_detail', pk=pk)

    listing = get_object_or_404(Listing, pk=pk)
    pending_exists = Booking.objects.filter(
        user=request.user,
        listing=listing,
        status=Booking.STATUS_PENDING,
    ).exists()

    if pending_exists:
        messages.warning(request, 'You already have a pending booking request for this listing.')
        return redirect('listings:booking_dashboard')

    Booking.objects.create(user=request.user, listing=listing)
    messages.success(request, 'Booking request submitted. You can track it on your dashboard.')
    return redirect('listings:booking_dashboard')


@login_required
def booking_dashboard(request):
    bookings = Booking.objects.filter(user=request.user).select_related('listing')
    return render(request, 'bookings/dashboard.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.status != Booking.STATUS_PENDING:
        messages.warning(request, 'Only pending bookings can be canceled.')
    else:
        booking.status = Booking.STATUS_CANCELLED
        booking.save(update_fields=['status', 'updated_at'])
        messages.success(request, 'Your booking request has been canceled.')
    return redirect('listings:booking_dashboard')

