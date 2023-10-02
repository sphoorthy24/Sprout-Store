# Sprout-Store
Features
Dynamic Website: The website is built using HTML, CSS, and Flask to create a dynamic and interactive user interface.

Database Integration: We have integrated MySQL using Flask to manage product, customer, and order data.

phpMyAdmin: The relational database is managed using phpMyAdmin, which provides an easy-to-use interface for database administration.

User Interface: We have crafted an intuitive, user-friendly interface to enhance the shopping experience

SQL Queries: SQL queries have been implemented for efficient data retrieval and management, ensuring that the website operates smoothly.

Front-End and Back-End Integration: The front-end and back-end components have been seamlessly integrated to create a fully functional online store.

Usage
Browse and search for products on the website.
Create an account or log in to an existing account.
Add products to your cart and proceed to checkout.
View and manage your orders.
Admins can manage products and customer orders.

Getting Started
Follow these instructions to get the project up and running on your local machine.

Prerequisites

Python: You will need Python installed on your machine. You can download it from Python's official website.

MySQL: Install MySQL and phpMyAdmin to manage the database. You can download them from MySQL's official website and phpMyAdmin's official website.

Installation :

Clone the repository to your local machine:
git clone https://github.com/your-username/sprouts-store.git

Navigate to the project directory:
cd sprouts-store

Create a virtual environment (optional but recommended):
python -m venv venv

Activate the virtual environment:
On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate


Install the required Python packages:

pip install -r requirements.txt

Set up the MySQL database using phpMyAdmin by importing the provided SQL schema file.

Configure the database connection in the Flask app. You can find the database configuration in the config.py file.

Run the Flask application:
flask run

The application should now be running locally. You can access it by opening a web browser and navigating to http://localhost:5000.
