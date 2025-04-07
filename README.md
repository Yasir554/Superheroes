# 🦸‍♀️ Superpower Management API

A RESTful Flask API to manage superheroes, their powers, and their power strengths. Built with Flask, SQLAlchemy, and SQLite, this project allows clients to create, read, and update data for heroes and their abilities.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Seeding the Database](#seeding-the-database)
- [Running the Server](#running-the-server)
- [API Endpoints](#api-endpoints)
- [Validation Rules](#validation-rules)
- [Example Usage](#example-usage)
- [Notes](#notes)
- [Author](#author)

## 🚀 Features

- List all heroes and their details
- Fetch specific hero information
- List all powers
- Fetch and update individual power data
- Assign powers to heroes with strength levels (Strong, Weak, Average)
- Seed database with sample data

## 📁 Project Structure

```bash
.
├── app.py            # Main application with API routes
├── models.py         # SQLAlchemy models and validations
├── seed.py           # Seeds the database with heroes and powers
├── Pipfile           # Project dependencies
└── migrations/       # Flask-Migrate migration folder (auto-generated)
```

## 📦 Requirements

- Python 3.8+
- pipenv

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/superpower-api.git
   cd superpower-api
   ```
2. **Install dependencies**
   ```bash
   pipenv install
   ```
3. **Activate the virtual environment**
   ```bash
   pipenv shell
   ```

## 🗄️ Database Setup

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

## 🌱 Seeding the Database

```bash
python seed.py
```

## ▶️ Running the Server

```bash
python app.py
```
The server will start at `http://localhost:5555`.

## 🔌 API Endpoints

### Root

- `GET /`  
  Returns a welcome message.

### Heroes

- `GET /heroes`  
  Returns a list of all heroes.

- `GET /heroes/<id>`  
  Returns detailed information about a specific hero.

### Powers

- `GET /powers`  
  Returns a list of all powers.

- `GET /powers/<id>`  
  Returns a specific power by ID.

- `PATCH /powers/<id>`  
  Update the description of a power.  
  **Request Body:**
  ```json
  {
    "description": "Updated description here"
  }
  ```

### Hero Powers

- `POST /hero_powers`  
  Assign a power to a hero with strength.  
  **Request Body:**
  ```json
  {
    "strength": "Strong",
    "power_id": 1,
    "hero_id": 3
  }
  ```

## ⚙️ Validation Rules

- Power description must be at least 20 characters.
- Strength must be one of: `"Strong"`, `"Weak"`, or `"Average"`.

## 🧪 Example Usage (Postman)

### Add a Power to a Hero

- **Endpoint:** `POST /hero_powers`  
- **Body:**
  ```json
  {
    "strength": "Strong",
    "hero_id": 1,
    "power_id": 2
  }
  ```

### Update a Power

- **Endpoint:** `PATCH /powers/1`  
- **Body:**
  ```json
  {
    "description": "Gives the ability to manipulate time and space"
  }
  ```

## 📌 Notes

- The project uses SQLite for local storage.
- All database models use SQLAlchemy and include serialization via `sqlalchemy-serializer`.

## 🧑‍💻 Author

Yasir Abass

