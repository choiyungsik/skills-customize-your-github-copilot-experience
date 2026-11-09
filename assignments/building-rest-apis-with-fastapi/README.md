# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API using FastAPI and learn how to define routes, validate inputs, and return JSON responses. Students will practice building a simple backend service that handles common API operations.

## 📝 Tasks

### 🛠️ Create a basic FastAPI app

#### Description
Set up a minimal FastAPI application and create your first endpoint to confirm the app is running correctly.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance
- Define a root endpoint that returns a welcome message
- Run the app locally with Uvicorn or the FastAPI development server
- Confirm the endpoint returns JSON data in the browser or with a client tool

### 🛠️ Build CRUD-style routes

#### Description
Add several endpoints to manage a simple collection of items, such as books, tasks, or students.

#### Requirements
Completed program should:

- Create an endpoint to list all items
- Create an endpoint to add a new item
- Create an endpoint to retrieve one item by ID
- Create an endpoint to update an existing item
- Create an endpoint to delete an item
- Return JSON responses with appropriate status codes

### 🛠️ Add validation and data models

#### Description
Use Pydantic models to validate request data and keep the API organized and predictable.

#### Requirements
Completed program should:

- Define a data model for the item structure
- Require fields such as `id`, `name`, and any other relevant values
- Return clear validation errors for invalid input
- Keep the API logic readable and maintainable with clear route names

