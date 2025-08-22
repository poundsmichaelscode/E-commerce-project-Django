

# 🛒 E-Commerce Platform (Admin Side)

This project is a **Django-based E-commerce Platform** focused on the **Admin Side** of operations. 
It provides administrators with the ability to manage products, categories, orders, customers,( and payments through a secure and scalable backend system.(future update) 



## 🚀 Features

### 🔑 Authentication & Security

* Admin login/logout system with Django’s built-in authentication.
* Role-based access control (Superuser, Staff).
* Secure session management.

### 📦 Product Management

* Add, edit, delete, and update products.
* Categorize products by category/brand.
* Upload product images.
* Manage product stock and availability.

### 🗂 Category & Brand Management

* Create and manage product categories.
* Add and organize brands for better filtering.

### 📑 Order Management

* View and track customer orders.
* Update order status (Pending, Shipped, Delivered, Cancelled).
* Generate invoices/receipts.

### 👥 Customer Management

* View registered users and their order history.
* Manage customer profiles.

### 💳 Payment & Transactions( to be added soon)

* Integration-ready with payment gateways (Stripe, PayPal, etc.).
* Track successful and failed transactions.

### 📊 Dashboard & Analytics (to be added soon)

* Overview of total sales, revenue, and active customers.
* Daily/weekly/monthly reports.



## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite3 (default), PostgreSQL/MySQL (recommended for production)
* **Frontend (Admin):** Django Admin + Bootstrap (customized)
* **Authentication:** Django Authentication System
* **Others:** Pillow (for image upload), Django REST Framework (optional API integration)

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/poundsmichaelscode/E-commerce-project-Django/
cd accounts
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Now visit **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)** to log in as Admin.

---

## 📂 Project Structure

```
ecommerce-admin/
│── ecommerce/           # Main project settings
│── shop/                # Core app (products, categories, orders, customers)
│── templates/           # Admin templates (customized if needed)
│── static/              # CSS, JS, images
│── media/               # Uploaded product images
│── manage.py            # Django project manager
│── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 🧪 Testing

Run tests using:

```bash
python manage.py test
```

---

## 📌 Future Improvements

* API endpoints for Mobile App/Frontend (Django REST Framework).
* Advanced reporting with charts/graphs.
* Role-based dashboards (Staff vs. Superadmin).
* Integration with multiple payment gateways.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

## 📜 License




