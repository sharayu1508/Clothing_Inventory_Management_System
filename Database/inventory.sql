CREATE DATABASE IF NOT EXISTS clothing_inventory;
USE clothing_inventory;

-- Suppliers Table
CREATE TABLE Suppliers (
    Supplier_ID INT AUTO_INCREMENT PRIMARY KEY,
    Supplier_Name VARCHAR(100) NOT NULL,
    Contact_Person VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address TEXT
);

-- Products Table
CREATE TABLE Products (
    Product_ID INT AUTO_INCREMENT PRIMARY KEY,
    Product_Name VARCHAR(100) NOT NULL,
    Category VARCHAR(50),
    Brand VARCHAR(50),
    Size VARCHAR(20),
    Color VARCHAR(30),
    Selling_Price DECIMAL(10,2),
    Stock INT DEFAULT 0,
    Supplier_ID INT,
    FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID)
);

-- Sales Table
CREATE TABLE Sales (
    Sale_ID INT AUTO_INCREMENT PRIMARY KEY,
    Product_ID INT,
    Customer_Name VARCHAR(100),
    Quantity INT,
    Selling_Price DECIMAL(10,2),
    Total_Amount DECIMAL(10,2),
    Sale_Date DATE,
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

-- Users Table 

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL
);