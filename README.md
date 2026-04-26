Bookstore Web Application

A full-stack Django application designed to manage books with secure authentication, role-based access control, and a RESTful API. This project demonstrates clean architecture, scalable design, and real-world backend development practices.

Overview

The Bookstore Application allows users to browse, create, update, and delete book records. It integrates authentication and authorization to ensure secure access, along with a REST API for structured data interaction.

Key Features
Core Functionality
Display all books on the homepage
View detailed information for each book
Create, update, and delete books (CRUD operations)
Authentication and Authorization
User registration and login system
Session-based authentication
Protected routes using login_required
Ownership-based permissions:
Only the user who created a book can edit or delete it
REST API (Django REST Framework)
Retrieve all books
Retrieve a single book by ID
API route discovery endpoint
Tech Stack
Backend:    Django (Python)
API:        Django REST Framework
Database:   SQLite
Frontend:   Django Templates with Bootstrap 5
Auth:       Django Built-in Authentication System
API Endpoints
GET /api/                → List all API routes  
GET /api/books/          → Retrieve all books  
GET /api/books/<id>/     → Retrieve a single book  
Sample Response
{
  "id": 1,
  "title": "Power Ranger",
  "author": "Kim Joson",
  "year": 2005,
  "rating": 10.0,
  "description": "people who have super powers",
  "posted_by": 1
}
Project Structure
bookstore/
│
├── books/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── __init__.py
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── bookstore/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
Setup and Installation
git clone https://github.com/yourusername/bookstore.git
cd bookstore

python -m venv venv
venv\Scripts\activate   # Windows

pip install django djangorestframework

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Usage
Homepage:   http://127.0.0.1:8000/
Admin:      http://127.0.0.1:8000/admin/
API:        http://127.0.0.1:8000/api/
Key Concepts Demonstrated
Django MVT (Model-View-Template) architecture
CRUD operations with database integration
Authentication and session management
Authorization and access control
REST API development and serialization
Error handling and validation
Clean and reusable template structure
Responsive UI using Bootstrap
Notes
db.sqlite3 is excluded from the repository
venv/ is ignored for clean project structure
Author

Kim Joson
