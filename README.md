# Scholarly API

This project creates a REST API for searching Google Scholar using the Scholarly Python package.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies: `pip install -r requirements.txt`
4. Create a `.env` file with your API key.
5. Run the application: `uvicorn app.main:app --reload`

## Usage

Visit `http://127.0.0.1:8000/docs` to see the Swagger UI and test the API.

## ------------------------------------------------------------------------------
Running the Project

    Clone the repository:

  ```  bash

git clone https://your-repository-url.git
cd scholarly_api

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Create a .env file with your API key.

Run the application:

uvicorn app.main:app --reload

Access the Swagger UI:
Open your browser and go to http://127.0.0.1:8000/docs.
```