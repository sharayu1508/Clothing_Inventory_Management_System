# 👕 Clothing Inventory Management System

A Python and MySQL based **Clothing Inventory Management System** developed to efficiently manage clothing store operations. The system provides role-based access for **Admin**, **User**, and **Guest (Consumer)** to manage suppliers, products, inventory, sales, and reports through a simple command-line interface.

---

# 📌 Problem Statement

Managing a clothing store manually is time-consuming and error-prone. Tracking products, suppliers, stock levels, and sales using paper records or spreadsheets can lead to inaccurate inventory management and inefficient business operations.

This project provides a digital solution that helps store owners efficiently manage their inventory, suppliers, and sales while providing secure role-based access to different users.

---

# ✨ Features

## 🤖 AI Chat Assistant
- AI-powered chatbot using Ollama (Llama 3.2)

## 🔐 Authentication & Authorization
- Admin Login
- User Login
- Guest (Consumer) Access without Login
- Role-Based Access Control

## 👨‍💼 Admin Features
- Supplier Management
  - Add Supplier
  - View Suppliers
  - Search Supplier
  - Update Supplier
  - Delete Supplier

- Product Management
  - Add Product
  - View Products
  - Search Product
  - Update Product
  - Delete Product

- Inventory Management
  - Stock In
  - Stock Out
  - View Inventory
  - Low Stock Report
  - Out of Stock Report

- Sales Management
  - Sell Products
  - Generate Bill
  - Update Stock Automatically
  - Sales History

- Reports
  - Product Reports
  - Inventory Reports
  - Sales Reports
  - PDF Report Generation

- User Management
  - Add New Admin/User

## 👤 User Features
- Login
- View Products
- Purchase Products
- Generate Bill

## 👥 Guest Features
- View Available Products
- Browse Products without Login

---

# 🛠 Technologies Used

## Programming Language
- Python 3.x

## Database
- MySQL

## Python Libraries
- mysql-connector-python
- tabulate
- reportlab

## Tools
- Visual Studio Code
- MySQL Workbench
- Git
- GitHub

---

# 📂 Folder Structure

```
Clothing_Inventory_Management_System/
│
├── Backend/
│   ├── main.py
│   ├── login.py
│   ├── database.py
│   ├── supplier.py
│   ├── product.py
│   ├── inventory.py
│   ├── sales.py
│   ├── reports.py
│   ├── consumer.py
│   ├── ai_chat.py
│   └── requirements.txt
│
├── Database/
│   └── inventory.sql
│
└── README.md
```

---

# 🗄 Database Design

The project uses the following database tables:

- Users
- Suppliers
- Products
- Sales

The database maintains relationships using foreign keys to ensure data integrity.

---

# 🚀 How to Run the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/sharayu1508/Clothing_Inventory_Management_System.git
```

## Step 2: Open the Project

```bash
cd Clothing_Inventory_Management_System
```

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 4: Create Database

- Open **MySQL Workbench**
- Run the **inventory.sql** file

## Step 5: Configure Database Connection

Update your MySQL credentials inside **database.py**

```python
host="localhost"
user="root"
password="your_password"
database="clothing_inventory"
```

## Step 6: Run the Project

```bash
python main.py
```

---

# 👨‍💻 User Roles

## 👨‍💼 Admin

- Manage Suppliers
- Manage Products
- Manage Inventory
- Manage Sales
- Generate Reports
- Add Users

---

## 👤 User

- Login
- View Products
- Purchase Products

---

## 👥 Guest

- View Available Products
- No Login Required

---

# 📊 Project Modules

- Login Module
- Supplier Management
- Product Management
- Inventory Management
- Sales Management
- Reports Module
- Guest Module
- Consumer (Guest) Module
- AI Chat Assistant Module

---

# 🔒 Security Features

- Login Authentication
- Role-Based Access Control
- Database Validation
- Input Validation

---

## 📈 Future Enhancements

- AI Assistant integrated with live MySQL database
- Barcode Scanner Integration
- QR Code Based Product Search
- Sales Analytics Dashboard
- Email Notifications
- Django Web Application
- Cloud Database Integration
- Mobile Application

---

# 👥 Team Member Details

| Team Member | Role | Responsibilities |
|-------------|------|------------------|
| **Sharayu Jadhav** | **Team Leader** | Login Module<br>Main Module<br>Database Connection<br>Database Design<br>Consumer (Guest) Module<br>AI Chat Assistant Module<br>Project Integration<br>GitHub Management<br>Testing & Debugging |
| **Viraj** | Team Member | Supplier Management Module |
| **Riddhi** | Team Member | Product Management Module |
| **Saksham** | Team Member | Inventory Management Module |
| **Sanskruti** | Team Member | Sales Management Module |
| **Shrikant** | Team Member | Reports Module | 

---

# 🎯 Project Outcome

The Clothing Inventory Management System simplifies inventory management by providing a centralized platform for managing products, suppliers, inventory, and sales. The system improves accuracy, reduces manual effort, and ensures secure access through role-based authentication.

---

# 📄 License

This project is developed for educational purposes as part of the Diploma in Computer Engineering curriculum.

---

## ⭐ If you found this project helpful, don't forget to Star ⭐ the repository!
