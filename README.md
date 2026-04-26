Bookstore Web Application

A full-stack Django application designed to manage books with authentication, authorization, and a REST API.

Overview

The Bookstore Application allows users to browse, create, update, and delete books. It includes secure login and role-based access control.

Key Features
Core Functionality
Display all books on homepage
View book details
Create, update, and delete books
Authentication and Authorization
User registration and login
Protected routes using login_required
Only the book owner can edit or delete
REST API
Get all books
Get single book by ID
API routes endpoint
Tech Stack
Backend:    Django (Python)
API:        Django REST Framework
Database:   SQLite
Frontend:   Django Templates + Bootstrap
Auth:       Django Built-in Authentication
API Endpoints
GET /api/
GET /api/books/
GET /api/books/<id>/
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
Setup
git clone https://github.com/yourusername/bookstore.git
cd bookstore

python -m venv venv
venv\Scripts\activate

pip install django djangorestframework

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Usage
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/
Notes
db.sqlite3 is not included
venv/ is ignored
Author

Kim Joson
