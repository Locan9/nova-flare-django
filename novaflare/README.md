# 🚀 NovaFlare (Django Edition)

NovaFlare is a web-based outfit recommendation platform that suggests stylish clothing combinations based on your available wardrobe and dynamic color compatibility rules. 

Originally built as a static frontend app, this version has been fully migrated to a robust **Django full-stack backend** featuring object-oriented matching architecture, a built-in SQLite database engine, and authenticated user wardrobe saving.

---

## 📂 Project Structure

```text
webdjang/
└── novaflare/
    ├── config/                  # Django project configuration settings & routing
    ├── wardrope/                # Main application folder
    │   ├── management/          # Custom admin terminal automation scripts
    │   ├── templates/           # Clean, modular server-rendered HTML views
    │   ├── matching_engine.py   # Object-Oriented matching engine class
    │   ├── models.py            # SQLite database table layouts
    │   └── views.py             # Authentication and form submission handlers
    ├── db.sqlite3               # Core local database
    ├── pyproject.toml           # Environment and dependency locks
    └── manage.py                # Django execution entrypoint
Markdown
# 🚀 NovaFlare (Django Edition)

NovaFlare is a web-based outfit recommendation platform that suggests stylish clothing combinations based on your available wardrobe and dynamic color compatibility rules. 

Originally built as a static frontend app, this version has been fully migrated to a robust **Django full-stack backend** featuring object-oriented matching architecture, a built-in SQLite database engine, and authenticated user wardrobe saving.

---

## 📂 Project Structure

```text
webdjang/
└── novaflare/
    ├── config/                  # Django project configuration settings & routing
    ├── wardrope/                # Main application folder
    │   ├── management/          # Custom admin terminal automation scripts
    │   ├── templates/           # Clean, modular server-rendered HTML views
    │   ├── matching_engine.py   # Object-Oriented matching engine class
    │   ├── models.py            # SQLite database table layouts
    │   └── views.py             # Authentication and form submission handlers
    ├── db.sqlite3               # Core local database
    ├── pyproject.toml           # Environment and dependency locks
    └── manage.py                # Django execution entrypoint
✨ Features
Smart Parsing Engine: Type your closet items using a clean colon-notation syntax; the backend converts it instantly into interactive data profiles.

Encapsulated Logic Matrix: An object-oriented NovaFlareEngine processing class parses inputs, evaluates 2-to-3 piece garment templates, and compares color relationships.

Database-Driven Rules: Outfits, clothing variations, and color matrices are stored cleanly inside database models rather than hardcoded vectors.

Persistent User Profiles: Built with standard Django encryption authentication. When registered users return, NovaFlare pulls their last-typed closet setup straight out of their personal UserProfile data entry automatically.

Galaxy Glassmorphic Design: Retains its aesthetic neon glow, nebula backdrops, and glassmorphic navigation layouts integrated directly into server-rendered Django templates.

🛠️ Technologies Used
Backend Framework: Django 6.0+ (Python)

Package Management: uv by Astral (ultra-fast dependency workspace provider)

Database: SQLite3

Frontend Foundations: HTML5, CSS3, Tailwind CSS CDN

▶️ How to Setup and Run
1. Prerequisites
Ensure you have Python and uv installed on your machine.

2. Environment Setup
Clone the repository, navigate into the root directory, and set up your locked dependencies using uv:

Bash
cd webdjang/novaflare
uv sync
3. Apply System Migrations
Build your native database structures locally:

Bash
uv run python manage.py makemigrations
uv run python manage.py migrate
4. Feed the Rule Engine (Database Seeding)
Run our custom data loading command to auto-populate all clothing presets, multi-garment outfits, and color vectors straight into your SQL tables:

Bash
uv run python manage.py load_data
5. Spawn an Admin Account
Create a terminal superuser credential to access the graphical administrative database backend panel:

Bash
uv run python manage.py createsuperuser
6. Ignition
Ignite the live development server:

Bash
uv run python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/.

📌 Engine Constraints & Rules
Valid Base Garments: tshirt, hoodie, casual shirt, light jacket, jeans, sweatpants, shorts, pants.

Color Range: green, blue, yellow, red, orange, purple, brown, black, white, silver.

Note: Custom descriptors must require light or dark prefix qualifiers (excepting uniform scales black, white, silver) to properly trigger exact dictionary compatibility validations.