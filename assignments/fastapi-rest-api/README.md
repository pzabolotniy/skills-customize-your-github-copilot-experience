# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement RESTful APIs using the FastAPI framework in Python. Practice creating endpoints, handling requests, and returning JSON responses.

## 📝 Tasks

### 🛠️ Project Setup & First Endpoint

#### Description
Set up a new FastAPI project and create your first API endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a main Python file to run the API
- Implement a root endpoint (`/`) that returns a JSON welcome message


### 🛠️ CRUD Operations for Items

#### Description
Add endpoints to perform Create, Read, Update, and Delete (CRUD) operations on a simple in-memory list of items.

#### Requirements
Completed program should:

- Implement endpoints for:
  - Creating a new item (POST `/items/`)
  - Listing all items (GET `/items/`)
  - Retrieving a single item by ID (GET `/items/{item_id}`)
  - Updating an item by ID (PUT `/items/{item_id}`)
  - Deleting an item by ID (DELETE `/items/{item_id}`)
- Use Pydantic models for request and response validation
- Return appropriate status codes and error messages

---
**Example Output:**
```
GET /items/
Response: [ { "id": 1, "name": "Book" }, { "id": 2, "name": "Pen" } ]
```
