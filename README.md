Shipment Management API

  This is a Django-based API for managing shipment records. The API supports different user roles, including Admin, Owner, and Consumer. It allows for various actions such as creating, updating, deleting, and viewing shipment details and performing category-based searches for shipments.
 Features
  - **User Roles**: Admin, Owner, and Consumer roles with different levels of access.
  - **CRUD Operations**: Create, Read, Update, and Delete shipment records.
  - **Search**: Search shipments by category.
  - **JWT Authentication**: Secure access to the API using JSON Web Tokens (JWT).
  - **Role-Based Access Control**: Only users with the proper role can perform specific actions.

Installation
  To get this project up and running locally, follow these steps:
Prerequisites
  - Python 3.x
  - Django
  - Django REST Framework
  - PostgreSQL (or any database of your choice)
Step 1: Clone the repository
  git clone https://github.com/Rhimanth/Django-rest_framework.git
  cd Django-rest_framework

Step 2: Set up the virtual environment
  python3 -m venv venv
  source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

Step 3: Install dependencies
  pip install -r requirements.txt

Step 4: Configure the database
  Make sure you have a PostgreSQL database set up (or modify the settings.py file for another database). Then, run the following commands to set up the database:
  python manage.py migrate

Step 5: Create a superuser (for Admin access)
  python manage.py createsuperuser
  Follow the prompts to create an admin user.

Step 6: Start the development server
  python manage.py runserver
  You can now access the API at http://127.0.0.1:8000/.
API Endpoints
    1. Token Generation
       	URL: /token/
          Method: POST
          Body: { "email": "user@example.com", "password": "password" }
          Description: Generates a JWT token for authenticated access.
    2. Search Shipments by Category
      URL: /search?category={category}
        Method: GET
        Description: Search for shipments by category (e.g., category=Electronics).
    3. View a Shipment
      URL: /view1/{shipmentId}/
        Method: GET
        Description: View details of a specific shipment by shipmentId. Requires authentication.
    4. Create a Shipment
      URL: /api2/
        Method: POST
        Body:
        {
          "shipmentId": "1002",
          "shipmentUser": "user2",
          "shipmentCategory": "Furniture",
          "shipmentQuantity": 5,
          "shipmentPrice": 1000
        }
        Description: Create a new shipment record. Requires authentication.
    5. Update a Shipment
      URL: /view1/{shipmentId}/
        Method: PUT
        Body:
        {
          "shipmentCategory": "Updated Category",
          "shipmentQuantity": 15,
          "shipmentPrice": 800
        }
        Description: Update details of a shipment. Requires authentication.
    6. Delete a Shipment
      URL: /view1/{shipmentId}/
        Method: DELETE
        Description: Delete a shipment. Requires authentication.
       
Tests
      The project includes a suite of test cases to ensure that the API works as expected. To run the tests:
    python manage.py test
        The test cases cover scenarios like:
        Token generation (valid and invalid credentials)
        Search functionality (with valid and invalid categories)
        User role-based access (ensuring only Admin users can access certain endpoints)
        Roles & Permissions
        Admin: Full access to create, update, delete, and view all shipments.
        Owner: Can view and update shipments owned by them.
        Consumer: Can only view shipments but cannot modify them.

Dependencies
  Django
  Django REST Framework
  djangorestframework-simplejwt (for JWT authentication)
  pytest (for running tests)
