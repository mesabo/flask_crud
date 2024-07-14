# Flask CRUD Application

This repository contains a Flask-based CRUD (Create, Read, Update, Delete) application designed to manage Todo items. The application leverages MongoDB for data storage and features a well-structured codebase with a clear separation of concerns.

## Features

- **CRUD Operations**: Full support for creating, reading, updating, and deleting Todo items.
- **RESTful API**: Exposes a RESTful API for interacting with the Todo items.
- **Swagger UI**: Integrated Swagger UI for easy API documentation and testing.
- **Auto-reload**: Flask development server is configured to auto-reload on code changes for efficient development.
- **Structured Codebase**: Organized into clearly defined directories for models, routes, services, procedures, utilities, and database configuration.

## Project Structure
.
├── CHANGELOG.md
├── README.md
├── pycache
│   └── app.cpython-312.pyc
├── src
│   ├── Database
│   │   └── init.py
│   ├── Models
│   │   └── init.py
│   ├── Procedures
│   │   └── init.py
│   ├── Routes
│   │   └── init.py
│   ├── Services
│   │   └── init.py
│   ├── Utils
│   │   └── init.py
│   └── init.py
├── app.py
└── tests
└── init.py

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/mesabo/flask_crud.git
    cd flask_crud
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root with the following content:
    ```
    MONGO_URL=mongodb://localhost:27017/?retryWrites=true&loadBalanced=false&serverSelectionTimeoutMS=5000&connectTimeoutMS=10000
    DB_URL=mongodb://localhost:27017/
    DB_NAME=Develop
    DB_USER=Developer00
    DB_PASSWORD=Developer2024-
    ```

5. **Run the application**:
    ```sh
    python src.py
    ```

6. **Access Swagger UI**:
    Open your browser and navigate to `http://127.0.0.1:5000/apidocs` to view and test the API endpoints.

## Running Tests

The project includes a suite of tests to ensure the functionality of the application. To run the tests, use:

```sh
pytest
```

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.