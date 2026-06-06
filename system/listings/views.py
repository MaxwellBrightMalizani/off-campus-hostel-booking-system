from types import SimpleNamespace

from django.shortcuts import render, get_object_or_404
from .models import Listing


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
    return render(request, 'listings/listing_detail.html', {'listing': listing})
