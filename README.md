Contact Book CLI 📇

A command‑line contact manager that evolved from an in‑memory toy into a database‑backed, ORM‑driven application.

✨ Key Features

Category

What you get

Persistent storage

SQLite database via Peewee ORM – contacts survive restarts

Full CRUD

Add / edit / delete / list contacts directly from the CLI

Validation

Phone (E.164), e‑mail, names – powered by a dedicated helper.py

UUID primary keys

Safer than auto‑increment IDs; ready for sync & merge

Atomic transactions

Every insert / edit / delete wrapped in db.atomic() – no half‑written rows

Clean architecture

 models ↔ repository ↔ menu layers; helpers stay framework‑agnostic

Python ≥ 3.10

Uses pattern‑matching (match…case) for menu navigation

Extensible

Same repo layer can point to PostgreSQL by changing DATABASE_URL

📦 Project structure

📂 desktop_app/
 ├─ helper.py          # validation utils (phone, email, etc.)
 ├─ models.py          # Peewee `Contact` model + DB init
 ├─ repository.py      # pure‑function CRUD layer
 ├─ menu.py            # CLI UI (previously main.py)
 └─ requirements.txt   # peewee, phonenumbers, email‑validator …

🚀 Quick start

python -m venv .venv && source .venv/bin/activate   # Win: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python menu.py

First run

The app will create contactlist.db and the contacts table automatically.

💬 Sample session

=== Contact Book ===
1. Add Contact
2. Edit Contact
3. Delete Contact
4. Show Contact list
5. Exit
Choose action: 1
First name: Ivan
Last name: Drago
Phone number: +48123123123
Email:
✅ Added: Ivan Drago (+48123123123)

🧠 What I learned during the refactor

ORM migration – swapping in‑memory storage for Peewee without breaking the UI

Transaction safety – using with db.atomic() to guarantee all‑or‑nothing writes

Repository pattern – decoupling business logic from CLI & from ORM details

Clean commit history – feat/, refactor/, style/ Conventional Commit flow

Error UX – thoughtful messages for duplicates & validation failures

Built as a personal learning project to level‑up Python architecture, ORM usage, and CLI UX.
