# ALX Travel App 0x01

This project builds on the previous `alx_travel_app_0x00` version by implementing fully functional API endpoints for managing travel listings and bookings. It also integrates automatic API documentation using Swagger.

## 📌 Objective

- Build CRUD API endpoints for Listings and Bookings.
- Ensure clean and RESTful API routing.
- Document all endpoints with Swagger (drf-yasg).

## 🚀 Features

### ✅ API Endpoints
- `ListingViewSet`: Handles GET, POST, PUT, DELETE for listings.
- `BookingViewSet`: Handles GET, POST, PUT, DELETE for bookings.
- All endpoints are served under `/api/` using a DRF router.

### 🔁 CRUD Operations
- Create a listing or booking
- Read (fetch) one or all
- Update (edit) an existing resource
- Delete a listing or booking

### 📄 Swagger Documentation
- Accessible at `/swagger/`
- Provides live interactive API interface using drf-yasg

## 🛠️ Setup Instructions

1. Duplicate the previous project:
   ```bash
   cp -r alx_travel_app_0x00 alx_travel_app_0x01
