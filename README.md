Product Catalog API
===================

This API allows you to manage a product catalog with functionalities for creating, reading, updating, and deleting products. It includes real-time inventory updates, a popularity score feature, and supports MySQL as the database.

Features
=========

CRUD operations for products
Search functionality for products by name and category
Real-time inventory update
Popularity score update based on sales
Test coverage for API endpoints

Tech Stack
Backend: Flask
Database: MySQL
Testing: Pytest

Installation Guide

1. Clone the repository:
   git clone <repo-url>
   cd product_catalog_api

2. Create a virtual environment:
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`

3. Install dependencies:
  pip install -r requirements.txt

4. Configure the MySQL Database:
   class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://<username>:<password>@localhost/product_catalog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
5. Initialize the database:
   flask db init
   flask db migrate
   flask db upgrade

6. Run the application:
   flask run

The server should start at http://127.0.0.1:5000.

API Endpoints
=============

1. Create a Product
   Endpoint: POST /products
   Request Body:
   
   {
    "name": "Sample Product",
    "description": "This is a sample product",
    "price": 19.99,
    "inventory_count": 50,
    "category": "Sample Category"
  }

  Response:

  {
    "id": 1,
    "name": "Sample Product",
    "description": "This is a sample product",
    "price": 19.99,
    "inventory_count": 50,
    "category": "Sample Category",
    "popularity_score": 0.0
  }

2. Get All Products (with Optional Search)
   
   Endpoint: GET /products
    Query Parameters:
    
      name: Filter by product name
      category: Filter by category
    Response:
   
     {
        "id": 1,
        "name": "Sample Product",
        "description": "This is a sample product",
        "price": 19.99,
        "inventory_count": 50,
        "category": "Sample Category",
        "popularity_score": 0.0
    }
   
 3. Get a Product by ID
    
    Endpoint: GET /products/<product_id>
    Response:
        {
          "id": 1,
          "name": "Sample Product",
          "description": "This is a sample product",
          "price": 19.99,
          "inventory_count": 50,
          "category": "Sample Category",
          "popularity_score": 0.0
      }

  4. Update a Product by ID
     Endpoint: PUT /products/<product_id>

     Request Body:
      {
          "name": "Updated Product",
          "description": "Updated description",
          "price": 24.99,
          "inventory_count": 40,
          "category": "Updated Category"
      }

     Response:
      {
          "id": 1,
          "name": "Updated Product",
          "description": "Updated description",
          "price": 24.99,
          "inventory_count": 40,
          "category": "Updated Category",
          "popularity_score": 0.0
      }

   5. Delete a Product by ID

      Endpoint: DELETE /products/<product_id>
      Response:
      
      {
          "message": "Product deleted"
      }

  6. Update Inventory Count
     
      Endpoint: PATCH /products/<product_id>/inventory
      Request Body:
      {
          "inventory_count": 45
      }

  7. Update Popularity Score

      Endpoint: PATCH /products/<product_id>/popularity

      Request Body:

       {
            "popularity_score": 5.0
       }
     
  9. Response:
    {
        "id": 1,
        "name": "Sample Product",
        "description": "This is a sample product",
        "price": 19.99,
        "inventory_count": 50,
        "category": "Sample Category",
        "popularity_score": 5.0
    }

Running Tests
==============
  To run tests for the API:
  
  Ensure that you're in the virtual environment.
  
  Run the following command:
    pytest --verbose








    









