# 🦸‍♀️ Superpower Management API

A RESTful Flask API to manage superheroes, their powers, and their power strengths. Built with Flask, SQLAlchemy, and SQLite, this project allows clients to create, read, and update data for heroes and their abilities.

---

## 🚀 Features

- List all heroes and their details
- Fetch specific hero information
- List all powers
- Fetch and update individual power data
- Assign powers to heroes with strength levels (Strong, Weak, Average)
- Seed database with sample data

---

## 📁 Project Structure

```bash
├── app.py            # Main application with API routes
├── models.py         # SQLAlchemy models and validations
├── seed.py           # Seeds the database with heroes and powers
├── Pipfile           # Project dependencies
└── migrations/       # Flask-Migrate migration folder (auto-generated)
📦 Requirements
Python 3.8+

pipenv

🛠 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/superpower-api.git
cd superpower-api
Install dependencies

bash
Copy
Edit
pipenv install
Activate virtual environment

bash
Copy
Edit
pipenv shell
Set up the database

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Seed the database

bash
Copy
Edit
python seed.py
Run the server

bash
Copy
Edit
python app.py
Server will start at http://localhost:5555.

🔌 API Endpoints
Root
GET /
Returns a welcome message.

Heroes
GET /heroes
Returns a list of all heroes.

GET /heroes/<id>
Returns detailed information about a specific hero.

Powers
GET /powers
Returns a list of all powers.

GET /powers/<id>
Returns a specific power by ID.

PATCH /powers/<id>
Update the description of a power.
Body JSON:

json
Copy
Edit
{
  "description": "Updated description here"
}
Hero Powers
POST /hero_powers
Assign a power to a hero with strength.
Body JSON:

json
Copy
Edit
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 3
}
⚙️ Validation Rules
Power description must be at least 20 characters.

strength must be either "Strong", "Weak", or "Average".

🧪 Example Usage (Postman)
Add a power to a hero:

POST to /hero_powers

Body:

json
Copy
Edit
{
  "strength": "Strong",
  "hero_id": 1,
  "power_id": 2
}
Update a power:

PATCH to /powers/1

Body:

json
Copy
Edit
{
  "description": "Gives the ability to manipulate time and space"
}
📌 Notes
The project uses SQLite for local storage.

All database models use SQLAlchemy and include serialization via sqlalchemy-serializer.

🧑‍💻 Author
Yasir Abass

