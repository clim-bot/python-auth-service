# python-auth-service

This is a Python authentication service built with Flask that demonstrates best practices in structuring a Python backend service using JWT tokens for authentication.

## Project Structure
```
python-auth-service/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── config.py
│   ├── services/
│   │   └── auth_service.py
│   └── utils/
│       └── jwt_utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_routes.py
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd python-auth-service
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the Flask server, run:

```bash
python run.py
```

The server will be available at http://127.0.0.1:5000/.

## API Endpoints
- Register a new user: POST /api/register
    - Request body: {"username": "user", "password": "pass"}
- Login an existing user: POST /api/login
    - Request body: {"username": "user", "password": "pass"}
The login endpoint returns a JWT token that can be used for authenticated requests.

## Testing
Run the unit tests with:
```bash
python -m unittest discover tests
```