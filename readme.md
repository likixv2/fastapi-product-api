# FastAPI Product API

A full-stack product management application built with FastAPI, SQLAlchemy, PostgreSQL, and React.

## Features

- Create products
- View all products
- View a single product by ID
- Update products
- Delete products
- PostgreSQL database integration
- RESTful API design
- React frontend
- CORS support for frontend-backend communication

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic

### Frontend
- React
- JavaScript
- CSS

## Project Structure

```text
fastapi_vid/
├── frontend/
├── database.py
├── database_models.py
├── models.py
├── main.py
└── README.md
```

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|----------|
| GET | /products | Get all products |
| GET | /products/{id} | Get a product by ID |
| POST | /products | Create a product |
| PUT | /products/{id} | Update a product |
| DELETE | /products/{id} | Delete a product |

## Running the Backend

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

Run the server:

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

## Running the Frontend

Navigate to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the React app:

```bash
npm start
```

Frontend runs at:

```text
http://localhost:3000
```

## Future Improvements

- User Authentication
- Product Search
- Pagination
- Image Uploads
- Docker Deployment
- Cloud Hosting

## Author

Likith