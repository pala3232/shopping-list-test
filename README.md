# Flask To-Do List App

A minimal Flask webapp to manage a shopping list using SQLite.

## System requirements

- Python 3.12+
- Docker (for containerization)
- Jenkins (for CI/CD, Jenkinsfile pipeline included)

## CI/CD Pipeline

This project includes a Jenkinsfile pipeline for unit testing and building a Docker container.

## Features

- Add, edit, delete, and list tasks
- SQLite database (created automatically)

## Setup (Docker)

1. Build and run image

```bash
   docker build -t testtodo .
   docker run -p 5000:5000 testtodo
   ```

2. Open your browser at [http://localhost:5000](http://localhost:5000)

## Setup (manual)

1. Create a Python virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Start the app:

   ```sh
   python app.py
   ```

4. Open your browser at [http://localhost:5000](http://localhost:5000)

## File Structure

- `app.py`: Main Flask app
- `templates/index.html`: HTML template
- `requirements.txt`: Python dependencies

## Notes

- The database file `todo.db` is created automatically in the project root.
- No authentication or user management is included.
