# auth-api-fastapi
Secure Authentication &amp; Authorization API with FastAPI + PostgreSQL + JWT
# 🔑 Authentication & Authorization API (FastAPI)  

A backend project that demonstrates **user authentication, authorization, and CRUD operations** using **FastAPI** and **PostgreSQL/SQLite**.  
This repo is designed to showcase backend fundamentals every company looks for: security, JWT, sessions, and role-based access control.  

---

## 📌 Why this project?  
Authentication and authorization are at the core of almost every application.  
This project highlights your understanding of:  
- Secure **user management**  
- **JWT-based authentication**  
- **Role-based access control** (admin vs. normal user)  
- **CRUD APIs** with database integration  

---

## 🚀 Features  
- User **registration & login**  
- JWT-based authentication (access token)  
- Role-based authorization (`admin` vs `user`)  
- CRUD APIs for a sample resource (e.g., blog posts)  
- Database support with **PostgreSQL** or **SQLite**  
- Auto-generated **Swagger UI docs** at `/docs`  

---

## 🛠 Tech Stack  
- **Backend:** FastAPI  
- **Database:** PostgreSQL (default) / SQLite (for local dev)  
- **ORM:** SQLAlchemy + Alembic (migrations)  
- **Auth:** JWT (python-jose) + bcrypt  
- **Validation:** Pydantic  

---

## 📂 Project Structure  

auth-api-fastapi/
│── alembic/ # DB migrations
│── app/
│ │── main.py # App entry point
│ │── config.py # Settings & secrets
│ │── database.py # DB connection
│ │── models.py # SQLAlchemy models
│ │── schemas.py # Pydantic schemas
│ │── utils.py # Hashing utils
│ │── auth/
│ │ │── routes.py # Signup & Login endpoints
│ │── crud/
│ │ │── routes.py # CRUD resource routes
│── requirements.txt
│── README.md
│── alembic.ini
