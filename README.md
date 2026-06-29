# Off-Campus Hostel Booking System — Getting Started (Database + Run)

This guide explains how to set up and run the project, including the **MySQL database setup** using the provided **`offcampus_db.sql`** file.

---

## 1) Prerequisites

- **Python** installed
- **MySQL** installed and running
- Access to a terminal

The app expects MySQL settings defined in:
- `system/system/settings.py`

Expected DB config (current values in the project):
- Database: `offcampus_db`
- Host: `localhost`
- Port: `3306`
- User: `root`
- Password: `academic1964_mysql`

Also note:
- `AUTH_USER_MODEL = 'accounts.CustomUser'` (custom user model)

---

## 2) Install dependencies

From the repository root (the folder containing `requirements.txt`):

```bash
pip install -r requirements.txt
```

---

## 3) Database setup (MySQL) — using `offcampus_db.sql`

### 3.1 Create the database

In MySQL (e.g., MySQL CLI):

```sql
CREATE DATABASE IF NOT EXISTS offcampus_db;
```

### 3.2 Import the dump file: `offcampus_db.sql`

The repository includes `offcampus_db.sql`.

Run this from the repo root:

```bash
mysql -u root -p offcampus_db < offcampus_db.sql
```

When prompted, enter the MySQL password: `academic1964_mysql`.

### What the dump contains

`offcampus_db.sql` is a full Django/MySQL dump created from this project. It includes:
- Django tables (auth/admin/contenttypes/sessions/migrations)
- Project tables:
  - `accounts_customuser`
  - `listings_listing`
  - `listings_booking`
- Sample data (so the UI can show listings and users immediately)

> Important: the dump contains `DROP TABLE IF EXISTS ...` statements.
> Importing it may remove existing tables in `offcampus_db`.

### 3.3 Confirm imports (quick check)

After import, verify key tables exist in MySQL:

```sql
SHOW TABLES;
```

You should see at least:
- `accounts_customuser`
- `listings_listing`
- `listings_booking`

---

## 4) Run the Django app

### 4.1 (Recommended) Run Django migrations

From the repo root:

```bash
python system\manage.py makemigrations
python system\manage.py migrate
```

### 4.2 Start the server

```bash
python system\manage.py runserver
```

Open:
- http://127.0.0.1:8000

---

## 5) Verify the database is being used

Run:

```bash
python system\manage.py check
```

Then:

```bash
python system\manage.py shell
```

Inside Django shell:

```python
from listings.models import Listing
Listing.objects.count()
```

If it returns `0`, either:
- the dump wasn’t imported into the expected DB, or
- your `settings.py` DB credentials/name don’t match.

---

## 6) How to test the main features (using seeded DB data)

After importing `offcampus_db.sql`, sample records exist. Common flows:

### Student
- Register/Login using the UI
- Browse hostels from `/listings/`
- Request booking from a listing detail page
- View bookings from `/dashboard/`
- Cancel a booking only when status is `pending`

### Owner
- Owner can manage properties via owner pages
- Owner can approve/decline booking requests only when booking is `pending`

---

## 7) Troubleshooting

### “Listings/hostels not showing”
- Confirm `listings_listing` has rows in MySQL.
- Open `/listings/` (shows all DB listings). The home page may show only featured/newest.

### Database connection errors
- Ensure MySQL is running.
- Ensure `system/system/settings.py` matches your MySQL credentials.

---

## 8) Required files (do not ignore)

- `offcampus_db.sql` → sets up schema + seed data in MySQL
- `system/system/settings.py` → MySQL connection + `AUTH_USER_MODEL`
- `system/manage.py` → migrate + runserver

---

## 9) What about the `*.json` dump files (e.g. `dump.json`, `sqlite_dump.json`)?

They are **not required for running the app**.

In this project, Django loads/creates data via **migrations** (and/or the MySQL dump you import). The `*.json` files shown in the repo are **example/alternate export dumps**:
- `dump.json` / `dump_latest.json` / `dump_listings_sqlite.json`
  - Django fixture-style JSON exports (they contain objects like `accounts.customuser`, `listings.listing`, `listings.booking`).
- `sqlite_dump.json`
  - Similar data export, typically intended for SQLite-based setups.

If you want, you *could* load them as Django fixtures (using `loaddata`), but the project’s main expected workflow is still:
1) import `offcampus_db.sql` into MySQL
2) run Django migrations
3) runserver


