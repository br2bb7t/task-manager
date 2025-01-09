# Task Manager Backend

## Description

This is the backend for the Task Manager application, developed using Django and configured to use MongoDB.

## Requirements

- **Python 3.8+**
- **MongoDB**
- **Poetry** (for dependency management)
- **Django** y **Django REST Framework**
- **Pymongo** (for MongoDB integration)

---

## Installation Steps

### 1. Clone the respository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/tu_usuario/task-manager.git
cd task-manager
```

### 2. Install Poetry
If you don't have Poetry installed, you can do so as follows:

On macOS/Linux:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

On Windows:

Follow the official instructions in the Poetry Docs.


### 3. Create and Activate a Virtual Environment with Poetry

Inside your project directory, run:

```bash
poetry install
poetry shell
```

### 4. Run the Server
To start the Django development server, run:

```bash
python manage.py runserver
```

The server will be available at http://localhost:8000/.

## API Usage
### API Documentation (Swagger)
Access the interactive API documentation using Swagger at:

```bash
http://localhost:8000/swagger/
```

## Endpoints

- **/api/tasks/** - Manage tasks (CRUD).
- **/swagger/** - Interactive API documentation.