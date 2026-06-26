from types import SimpleNamespace

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Listing, Booking


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
        
        # Search functionality
        search_query = request.GET.get('search', '')
        if search_query:
            listings = [
                l for l in listings 
                if search_query.lower() in l.title.lower() or 
                   search_query.lower() in l.address.lower()
            ]
    except Exception:
        listings = DEFAULT_LISTINGS
        search_query = ''
    
    return render(request, 'listings/listing_list.html', {
        'listings': listings,
        'search_query': search_query
    })


def listing_detail(request, pk):
    try:
        listing = get_object_or_404(Listing, pk=pk)
    except Exception:
        listing = next((item for item in DEFAULT_LISTINGS if item.id == pk), None)
        if listing is None:
            raise
    
    user_booking = None
    if request.user.is_authenticated:
        try:
            user_booking = Booking.objects.filter(
                student=request.user, 
                listing=listing
            ).first()
        except:
            pass
    
    return render(request, 'listings/listing_detail.html', {
        'listing': listing,
        'user_booking': user_booking
    })


@login_required(login_url='listings:home')
def booking_create(request, pk):
    """Create a new booking request"""
    listing = get_object_or_404(Listing, pk=pk)
    
    # Check if user already has a pending/confirmed booking for this listing
    existing_booking = Booking.objects.filter(
        student=request.user,
        listing=listing,
        status__in=['pending', 'confirmed']
    ).first()
    
    if existing_booking:
        messages.warning(request, 'You already have a booking request for this hostel.')
        return redirect('listings:listing_detail', pk=pk)
    
    if request.method == 'POST':
        try:
            check_in_date = request.POST.get('check_in_date')
            check_out_date = request.POST.get('check_out_date')
            number_of_rooms = int(request.POST.get('number_of_rooms', 1))
            notes = request.POST.get('notes', '')
            
            # Create booking
            booking = Booking.objects.create(
                student=request.user,
                listing=listing,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                number_of_rooms=number_of_rooms,
                notes=notes,
                status='pending'
            )
            
            messages.success(
                request, 
                f'Booking request submitted for {listing.title}! Check your dashboard for status.'
            )
            return redirect('student:bookings')
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
            return redirect('listings:listing_detail', pk=pk)
    
    return render(request, 'bookings/book.html', {
        'listing': listing
    })


@login_required
def student_bookings(request):
    """View all bookings for logged-in student"""
    try:
        bookings = Booking.objects.filter(student=request.user)
    except:
        bookings = []
    
    return render(request, 'student/bookings.html', {
        'bookings': bookings
    })


@login_required
def owner_booking_requests(request):
    """View all booking requests for listings owned by this user (would need an owner field)"""
    # For now, this shows all pending bookings - in production, filter by owner
    try:
        # Get all listings first (simplified - assumes user can see all for now)
        all_bookings = Booking.objects.filter(status='pending')
    except:
        all_bookings = []
    
    return render(request, 'owner/booking_requests.html', {
        'bookings': all_bookings
    })
