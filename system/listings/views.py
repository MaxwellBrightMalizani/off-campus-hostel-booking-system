from types import SimpleNamespace

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from accounts.decorators import owner_required

from .forms import ListingForm
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

    # Prefer the DB record; fall back to DEFAULT_LISTINGS so booking works
    # even when the DB is empty.
    try:
        listing = get_object_or_404(Listing, pk=pk)
    except Exception:
        # DEFAULT_LISTINGS are SimpleNamespace objects (not Listing models).
        # Create missing Listing rows in DB so Booking FK constraints work.
        from django.db import transaction

        defaults = next((item for item in DEFAULT_LISTINGS if item.id == pk), None)
        if defaults is None:
            from django.http import Http404
            raise Http404('Listing not found')

        with transaction.atomic():
            listing, created = Listing.objects.get_or_create(
                pk=defaults.pk,
                defaults={
                    'title': defaults.title,
                    'description': defaults.description,
                    'price': defaults.price,
                    'address': defaults.address,
                },
            )


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


@owner_required
def owner_dashboard(request):
    listings = Listing.objects.filter(owner=request.user).prefetch_related('bookings')
    bookings = Booking.objects.filter(listing__owner=request.user).select_related('listing', 'user')
    return render(
        request,
        'owner/dashboard.html',
        {
            'listings': listings,
            'bookings': bookings,
        },
    )


@owner_required
def owner_booking_decide(request, booking_id):
    booking = get_object_or_404(
        Booking,
        pk=booking_id,
        listing__owner=request.user,
    )

    if request.method != 'POST':
        return redirect('listings:owner_dashboard')

    action = request.POST.get('action')
    if booking.status != Booking.STATUS_PENDING:
        messages.warning(request, 'Only pending requests can be updated.')
        return redirect('listings:owner_dashboard')

    if action == 'approve':
        booking.status = Booking.STATUS_APPROVED
        booking.save(update_fields=['status', 'updated_at'])
        messages.success(request, 'Booking request approved.')
    elif action == 'decline':
        booking.status = Booking.STATUS_DECLINED
        booking.save(update_fields=['status', 'updated_at'])
        messages.success(request, 'Booking request declined.')
    else:
        messages.error(request, 'Invalid action.')

    return redirect('listings:owner_dashboard')


@owner_required
def owner_property_list(request):
    listings = Listing.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'owner/properties.html', {'listings': listings})


@owner_required
def owner_property_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            messages.success(request, 'Hostel details created.')
            return redirect('listings:owner_property_list')
    else:
        form = ListingForm()

    return render(request, 'owner/property_form.html', {'form': form, 'mode': 'create'})


@owner_required
def owner_property_update(request, pk):
    listing = get_object_or_404(Listing, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hostel details updated.')
            return redirect('listings:owner_property_list')
    else:
        form = ListingForm(instance=listing)

    return render(request, 'owner/property_form.html', {'form': form, 'mode': 'edit', 'listing': listing})


