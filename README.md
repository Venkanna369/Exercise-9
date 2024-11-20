
# FastAPI Exercise 9

## 1) What is a Schema?

In FastAPI, a schema is like a blueprint that defines the structure of your data. It specifies what kind of data your API should accept and return, along with any rules or constraints. For example, FastAPI uses Pydantic models to define these schemas. This helps ensure that the data flowing through your API is always in the right format.

---

## 2) What is the OpenAPI schema created for this project so far?

The OpenAPI schema for this project includes the `/customers/{id}` endpoint. This schema defines:

- **Request Method**: `GET`
- **Path Parameter**: `id` (must be an integer)
- **Expected Response**: A JSON object with these fields:
  - `id`: The customer's unique identifier.
  - `phone`: The customer's phone number.
  - `name`: The customer's name.
- **Error Responses**:
  - `404 Not Found`: If a customer with the given `id` doesn’t exist.

You can check out the schema in JSON format by visiting this URL in your browser: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json).

---

##  3) How does FastAPI make sure your REST API is Uniform?

FastAPI does a great job of keeping your REST API consistent by providing:

1. **Type Validation**: It uses Python type hints to validate the data automatically. You don't have to write extra validation logic.
2. **Automatic Documentation**: FastAPI generates Swagger UI and OpenAPI documentation for your endpoints, so you always have a clear reference for how your API works.
3. **Error Handling**: It ensures that errors like invalid input or missing resources are handled with proper status codes and messages.
4. **Standards Compliance**: FastAPI follows REST API best practices, making it easy to keep your API predictable and professional.

---

## 4) What was the hardest part of getting FastAPI to work?

Getting started with FastAPI is pretty straightforward, but there were a few tricky parts:

- **Setting Up the Environment**: Making sure all dependencies were installed correctly and the virtual environment was set up properly.
- **Path Parameters**: Understanding how to work with dynamic paths like `/customers/{id}` and ensuring they accept the right type of data.
- **Testing Endpoints**: Learning to use tools like Swagger UI and Postman to test and debug endpoints took some practice, especially for verifying edge cases.

---

## Project Overview

This project demonstrates the use of **FastAPI** to create a simple REST API that retrieves customer information by their unique ID. The API is built using Python, FastAPI, and Uvicorn.

The `/customers` endpoint allows you to fetch customer details like `id`, `phone`, and `name`. Additionally, the API provides a root endpoint `/` with a welcome message.

---

## Features

- Retrieve customer information using a RESTful API.
- Interactive documentation via Swagger UI (`/docs`).
- Auto-generated OpenAPI schema (`/openapi.json`).
- Lightweight and fast server using **Uvicorn**.

---

## Requirements

- Python 3.9+
- Virtual environment setup (recommended).

---

## Installation and Setup

### Clone the Repository
```bash
git clone <repository-url>
cd Exercise-9
```

### Create and Activate a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### Install Dependencies
Create a `requirements.txt` file with the following content:
```plaintext
fastapi
uvicorn[standard]
pydantic
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### Run the Application
Start the server with:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Access the API
- **Base URL:** `http://127.0.0.1:8000` or `http://0.0.0.0:8000`
- **API Documentation:** `http://127.0.0.1:8000/docs`
- **OpenAPI Schema:** `http://127.0.0.1:8000/openapi.json`

---

## API Endpoints

### Root Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "message": "Welcome to the FastAPI application. Use /customers/{id} to fetch customer data."
  }
  ```

### Customer Endpoint
- **URL:** `/customers/{id}`
- **Method:** `GET`
- **Path Parameter:**
  - `id` (int): Unique ID of the customer.
- **Response:**
  - For a valid `id`:
    ```json
    {
      "id": 0,
      "phone": "609-555-0124",
      "name": "Karl"
    }
    ```
  - For an invalid `id`:
    ```json
    {
      "detail": "Customer not found"
    }
    ```

---

## Logs from Execution

### Server Logs
```bash
INFO:     Will watch for changes in these directories: ['/workspaces/Exercise-9']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [16167] using StatReload
INFO:     Started server process [16169]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### Example cURL Requests
```bash
curl -X GET "http://0.0.0.0:8000/"
{"message":"Welcome to the FastAPI application. Use /customers/{id} to fetch customer data."}

curl -X GET "http://0.0.0.0:8000/customers/0"
{"id":0,"phone":"609-555-0124","name":"Karl"}

curl -X GET "http://0.0.0.0:8000/customers/1"
{"id":1,"phone":"609-555-1234","name":"Mike"}

curl -X GET "http://0.0.0.0:8000/customers/3"
{"id":3,"phone":"609-555-4302","name":"Ryan"}
```

## Testing the API

### Swagger UI
- Open `http://127.0.0.1:8000/docs` to test the API interactively.

### cURL Requests
- Run the following commands in the terminal:
  ```bash
  curl -X GET "http://127.0.0.1:8000/"
  curl -X GET "http://127.0.0.1:8000/customers/0"
  curl -X GET "http://127.0.0.1:8000/customers/3"
  ```
---

