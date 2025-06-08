# ZEDPOS (Point of Sale System)

Welcome to **ZEDPOS**, a web-based Point of Sale (POS) system built with Python and Django. This platform is designed to help small to medium-sized businesses manage sales, inventory, and customers efficiently through a clean and responsive user interface.

🔗 **Live Demo:** [zedpos.pythonanywhere.com](https://zedpos.pythonanywhere.com)

---

## 🚀 Features

* 🔐 User authentication and access control
* 🛒 Product management
* 💰 Sales tracking with invoices/receipts
* 📊 Dashboard for daily summaries and reports
* 🔎 Real-time search and filtering
* 📦 Category and stock-level management
* 💻 Responsive design with HTML, CSS, and JavaScript

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, JavaScript
* **Database:** SQLite (can be upgraded to PostgreSQL or MySQL)
* **Hosting:** PythonAnywhere


## ⚙️ Installation (Local Setup)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/usmonaliyev-uz/zedpos.git
   cd zedpos
   ```

2. **Create and activate virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the server:**

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/`

---

## 🧑‍💻 Admin Access

To create a superuser for admin access:

```bash
python manage.py createsuperuser
```

Then log in at `/admin/`

