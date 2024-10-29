# inventory_management

## Introduction

The **Inventory Management System** is designed to help businesses effectively manage their inventory by tracking products, monitoring stock levels, and alerting users when stock falls below a certain threshold. This system provides a comprehensive API built with Django REST Framework, enabling seamless integration with other applications and facilitating easy access to inventory data.

### Key Features

- **Product Management**: Add, update, and delete products in the inventory, along with detailed information such as price, quantity, and supplier details.
- **Stock Tracking**: Monitor stock levels in real-time, ensuring that products are restocked before running out.
- **Low Stock Alerts**: Automatically trigger alerts when product quantities fall below a predefined threshold, helping to avoid stockouts.
- **Reporting**: Generate reports to analyze total inventory value, stock levels, and filter products by category and supplier.
- **User Authentication**: Secure API endpoints with user authentication, ensuring that only authorized personnel can manage inventory.

This project aims to streamline inventory management processes and improve operational efficiency for businesses of all sizes.

## Tools Required

To run the **Inventory Management System**, the following tools and technologies are required:

- **Python**: Ensure you have Python 3.6 or higher installed on your machine. Python is the primary programming language used for the development of this project.

- **Django**: This project is built on Django, a high-level web framework that enables rapid development of secure and maintainable websites.

- **Django REST Framework**: A powerful toolkit for building Web APIs in Django, providing features such as serialization, authentication, and view sets.

- **PostgreSQL**: An open-source relational database management system used to store the application's data. Make sure to have PostgreSQL installed and running.

- **Docker**: A platform for developing, shipping, and running applications in containers. It helps to package the application and its dependencies into a container for consistent environments.

### Additional Tools

- **Docker Compose**: A tool for defining and running multi-container Docker applications. It allows you to configure your application services in a single `docker-compose.yml` file.


### Clone the Repository

To get started with the Inventory Management System, first clone the repository to your local machine using Git:

```bash
git clone https://github.com/vimal0207/inventory_management.git
cd inventory_management
```
### Create and Configure the `.env` File

1. **Create the `.env` File**: In the root directory of your cloned repository, create a file named `.env`.

2. **Add Configuration Data**: Open the `.env` file and add the following environment variables:

   ```env
   ENVIRONMENT="LOCAL"
   SERVER_BASE_URL="http://0.0.0.0:8000"
   SECRET_KEY="django-insecure-sdpmd%#ecke&1ctef0e-9sxz!i$!k3q=-(v3q+*+@z#x_o0+$t"

   ALLOWED_HOSTS="*"
   CSRF_TRUSTED_ORIGINS="http://0.0.0.0:8000"
   CORS_ALLOWED_ORIGINS="http://0.0.0.0"

   POSTGRES_ENGINE="django.db.backends.postgresql"
   POSTGRES_DB="inventory_management_db"
   POSTGRES_USER="postgres"
   POSTGRES_PASSWORD="postgres"
   POSTGRES_HOST="db"
   POSTGRES_PORT=5432
   ```
## Creating a docker build

To simplify your Docker setup and use the local Docker Compose configuration, you can create a symbolic link to the `local.yml` file. Follow these steps:

### Step 1: Navigate to the Project Directory

Open your terminal and navigate to the root directory of your project where your `docker` folder is located:

```bash
cd path/to/your/inventory_management

## Step 2: Create the Symbolic Link

Use the following command to create a symbolic link named `docker-compose.override.yml` that points to the `local.yml` file in the `docker/compose` directory:

```bash
ln -s docker/compose/local.yml docker-compose.override.yml

## Step 3: Build the Project

To build the project using Docker, follow these steps:

1. **Ensure Docker is Running**: Make sure Docker is running on your machine.

2. **Build the Docker Containers**: Run the following command in your project directory to build the Docker containers defined in your `docker-compose.yml`:

   ```bash
   docker-compose build


## Step 4: Run the Build

To run the build for your Inventory Management System, follow these steps:

1. **Open a Terminal**: Navigate to your project directory where the `docker-compose.yml` file is located.

2. **Build the Project**: Run the following command to build the project using Docker:

   ```bash
   docker-compose up
```
## API Documentation

This project uses **Swagger** to generate API documentation for easy reference and testing.

1. **Accessing Swagger Documentation**: Once your application is running, you can access the Swagger UI by navigating to:


This page provides a user-friendly interface for exploring the available API endpoints, viewing request/response formats, and testing API calls.

2. **Generating API Documentation**: The documentation is automatically generated based on your API views and serializers. Ensure that you have the necessary decorators in your views to enable Swagger documentation, such as `@swagger_auto_schema`.

3. **Viewing Endpoints**: In the Swagger UI, you'll find a list of all the available endpoints. You can click on each endpoint to expand and see details such as:

- **HTTP Method**: The type of request (GET, POST, PUT, DELETE).
- **Path**: The URL path of the endpoint.
- **Parameters**: Any query parameters, path parameters, or request bodies required.
- **Responses**: Possible response codes and their formats.

4. **Testing APIs**: You can use the Swagger UI to test the API endpoints directly. Fill in any required parameters and click the "Try it out!" button to see the responses.

By using Swagger, you can efficiently manage and document your API, making it easier for developers and users to understand and utilize your Inventory Management System.


## Creating a Superuser

To access the Django admin panel and manage the inventory system, you'll need to create a superuser account. Follow these steps:

1. **Open a Terminal**: Make sure you are in the project directory where your `docker-compose.yml` file is located.

2. **Run the Django Shell**: Use the following command to access the Django shell inside your Docker container:

   ```bash
   docker-compose exec inventory_management_app python manage.py createsuperuser
```
