# FastAPI Product Management API

A clean, production-ready REST API designed for product inventory management, built using **FastAPI**, **SQLAlchemy ORM**, and **Pydantic** data validation, with **PostgreSQL** as the database engine.

---

## 🚀 Features

* **Full CRUD Support**: Complete endpoints to create, read, update, and delete products dynamically.
* **Robust Data Validation**: Leverages Pydantic type annotations to enforce data constraints before processing.
* **Automated Table Provisioning**: Automatically generates database tables in PostgreSQL upon startup using SQLAlchemy's metadata bind.
* **Smart Data Seeding**: Evaluates if the target table is empty on startup and automatically seeds initial mock product records.
* **Leaking Prevention**: Uses FastAPI’s dependency injection (`Depends`) to open and close sessions explicitly per request lifecycle.

---

## 📁 Repository Architecture

```text
├── main.py              # Application initialization, core routes, and seeding logic
├── models.py            # Pydantic schemas for request validation and serialization
├── database_models.py   # SQLAlchemy ORM models mapping to the database schema
└── database.py          # Session configurations, engine initialization, and declarative base
