# SuperMarket Backend API

This is the Django REST Framework-based backend for the SuperMarket application. It handles product management, discount logic, cart processing, and inventory updates.

---

## Tech Stack

- Python 
- Django 
- Django REST Framework
- PostgreSQL

## Getting Started

### 1. Clone the Repo

1. git clone git@github-backend:your-username/supermart-backend.git
2. cd supermart-backend
3. python3 -m venv env
4. source env/bin/activate
5. pip install -r requirements.txt
6. Setup PostgreSQL on local (Install Postgresql and Create Database and User)
7. python manage.py makemigrations
8. python manage.py migrate
9. python manage.py runserver

## API Endpoints

Method	Endpoint	    Description
GET	    /api/products/	List all products
POST	/api/cart/add/	Add product to cart
POST	/api/checkout/	Checkout and calculate

