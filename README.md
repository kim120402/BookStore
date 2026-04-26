# Bookstore Web Application

A full-stack Django application designed to manage books with authentication, authorization, and a REST API.

---

## Overview

The Bookstore Application allows users to browse, create, update, and delete books. It includes secure login and role-based access control.

---

## Key Features

### Core Functionality
- Display all books on homepage  
- View book details  
- Create, update, and delete books  

### Authentication and Authorization
- User registration and login  
- Protected routes using `login_required`  
- Only the book owner can edit or delete  

### REST API
- Get all books  
- Get single book by ID  
- API routes endpoint  

---

## Tech Stack
Backend: Django (Python)
API: Django REST Framework
Database: SQLite
Frontend: Django Templates + Bootstrap
Auth: Django Built-in Authentication


---

## API Endpoints
GET /api/
GET /api/books/
GET /api/books/<id>/

---

## Project Structure
bookstore/
│
├── books/
│ ├── api/
│ │ ├── serializers.py
│ │ ├── views.py
│ │ ├── urls.py
│ │ └── init.py
│ ├── templates/
│ ├── models.py
│ ├── views.py
│ └── urls.py
│
├── bookstore/
│ ├── settings.py
│ └── urls.py
│
└── manage.py

---

## Setup


git clone https://github.com/kim120402/bookstore.git

cd bookstore

python -m venv venv
venv\Scripts\activate

pip install django djangorestframework

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

---## Usage

http://127.0.0.1:8000/
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/

## Screenshots
### Homepage
![Homepage]<img width="1919" height="995" alt="image" src="https://github.com/user-attachments/assets/d44577c9-7664-4275-be6a-eb72893a7009" />

### Book Detail
![Book Detail](screenshots/detail.png)

### Add Book
![Add Book](screenshots/add.png)

### Login
![Login](screenshots/login.png)

### API Output
![API](screenshots/api.png)
