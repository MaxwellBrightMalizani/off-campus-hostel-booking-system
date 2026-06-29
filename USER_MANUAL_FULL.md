# Off-Campus Hostel Booking System — Full User Manual

## 1. Overview
The **Off-Campus Hostel Booking System** is a web application that helps:
- **Students** browse hostel listings and submit booking requests.
- **Hostel Owners** manage their hostel listings and review/approve/decline booking requests.

### Roles and Permissions
- **Student**
  - Can view listings
  - Can request a booking
  - Can view booking dashboard
  - Can cancel only **pending** booking requests
- **Hostel Owner**
  - Can create/update hostel listings
  - Can view incoming booking requests
  - Can approve/decline only **pending** booking requests
  - Cannot create/cancel booking requests as a student

## 2. Requirements
- Python + Django
- A working database configuration (as configured in `system/system/settings.py`)
- Internet connection for Bootstrap/FontAwesome CDN assets

## 3. Getting Started
### 3.1 Install dependencies
```bash
pip install -r requirements.txt
```

### 3.2 Apply migrations
```bash
python system\manage.py migrate
```

### 3.3 Run the server
```bash
python system\manage.py runserver
```

### 3.4 Open the application
Visit:
- **http://127.0.0.1:8000**

## 4. Authentication
### 4.1 Register (Student)
1. Click **Register** from the navigation bar.
2. Complete the registration form.
3. Submit to create your account.

> Note: The registration UI is intended for **students**.

### 4.2 Login
1. Click **Login**.
2. Enter your email and password.
3. Submit.

### 4.3 Logout
- Use **Logout** in the user dropdown menu.

## 5. Navigation (What you can do on each page)

### Home
- URL: `/` (route name: `listings:home`)
- Purpose: Shows featured/listed hostels.

### Listings
- URL: `/listings/` (route name: `listings:listing_list`)
- Purpose: Shows **all hostel listings** stored in the database.

### Listing Details
- URL: `/listings/<id>/` (route name: `listings:listing_detail`)
- Purpose:
  - View the hostel information (title, address, description, price)
  - If you are logged in as a student, you can request a booking

### My Dashboard (Student)
- URL: `/dashboard/` (route name: `listings:booking_dashboard`)
- Purpose:
  - View your booking requests
  - Cancel bookings that are still **pending**

### Owner Dashboard
- URL: `/owner/dashboard/` (route name: `listings:owner_dashboard`)
- Purpose:
  - View your hostel listings
  - View booking requests from students for your hostels
  - Approve/decline pending requests

### Owner Properties
- URL: `/owner/properties/` (route name: `listings:owner_property_list`)
- Purpose:
  - View, create, and edit your hostel listings

## 6. Student Guide

### 6.1 Browse Hostels
1. Open **Listings**.
2. Choose a hostel to open its **Listing Details** page.

### 6.2 Request a Booking
On a **Listing Details** page:
1. If you have no pending booking for that hostel, click **Request Booking**.
2. You will be redirected to your **My Dashboard**.

System behavior:
- Booking request is created with status: **pending**
- Your dashboard will show the request.

### 6.3 View My Booking Dashboard
1. Click **My Dashboard** (top navigation).
2. You’ll see all your bookings with their statuses:
   - pending
   - approved
   - declined
   - cancelled

### 6.4 Cancel a Pending Booking
1. Open **My Dashboard**.
2. Find a booking with status **pending**.
3. Click **Cancel**.

Rules:
- Only **pending** requests can be canceled.
- Approved/declined bookings cannot be canceled.

## 7. Hostel Owner Guide

### 7.1 Access Owner Dashboard
1. Log in as an owner.
2. Click **Owner Dashboard** from the navigation.

### 7.2 Manage Your Hostel Listings
On **Owner Properties**:
- Create a hostel listing
- Edit a hostel listing

Owner changes update how hostels appear to students.

### 7.3 Review Booking Requests
1. Open **Owner Dashboard**.
2. View bookings submitted by students for your hostels.
3. For each booking request with status **pending**:
   - Click **Approve** to set status to **approved**
   - Click **Decline** to set status to **declined**

Rules:
- Only **pending** requests can be approved/declined.

## 8. Theme Toggle (Dark Mode)
The navigation bar includes a theme toggle button:
- Click the button to switch between light and dark themes.
- The choice is saved in `localStorage` so it persists after reload.

## 9. Common Issues / Troubleshooting

### 9.1 Theme toggle does not work
- Refresh the page.
- Ensure JavaScript is enabled in your browser.
- Hard refresh (Ctrl+F5) can help if caching occurred.

### 9.2 Hostels not showing
Possible causes:
- The database table `Listing` might be empty or not migrated.
- You are viewing a page that shows only featured/sliced listings.

Recommended checks:
- Visit **Listings** to view **all** listings.
- Visit **Home** to view featured listings.

### 9.3 Booking actions fail
- Ensure you are logged in.
- Ensure your account is a **student** for booking creation/cancellation.
- Ensure booking status rules are followed (cancel pending only).

## 10. Admin Notes (Optional)
Admin features depend on how Django admin is configured in your environment.
If you want owners created, use either:
- Django admin
- database seeding scripts

## 11. Data Model Summary

### Listing
- owner (ForeignKey to user)
- title
- description
- price
- address
- created_at

### Booking
- user (student)
- listing (hostel)
- status: pending/approved/declined/cancelled
- created_at
- updated_at

## 12. File/Route Reference (for developers)
- `system/listings/views.py` — listing + booking + owner pages
- `system/listings/models.py` — Listing and Booking models
- `system/listings/urls.py` — route definitions
- `system/templates/` — page templates
- `system/static/` — CSS and JavaScript

---
### Last Updated
(Use your project’s date when publishing.)

