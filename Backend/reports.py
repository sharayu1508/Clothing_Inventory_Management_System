from database import get_connection

def view_all_products():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()

    print("\n===== ALL PRODUCTS =====")
    for row in data:
        print(row)

    cursor.close()
    conn.close()


def search_product():
    pid = input("Enter Product ID : ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE Product_ID=%s", (pid,))
    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Product Not Found")

    cursor.close()
    conn.close()


def product_details():
    pid = input("Enter Product ID : ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE Product_ID=%s", (pid,))
    row = cursor.fetchone()

    if row:
        print("\n===== PRODUCT DETAILS =====")
        print("ID :", row[0])
        print("Name :", row[1])
        print("Category :", row[2])
        print("Brand :", row[3])
        print("Size :", row[4])
        print("Color :", row[5])
        print("Price :", row[6])
        print("Stock :", row[7])
    else:
        print("Product Not Found")

    cursor.close()
    conn.close()


def low_stock():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE Stock < 10")

    print("\n===== LOW STOCK REPORT =====")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


def out_of_stock():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE Stock = 0")

    print("\n===== OUT OF STOCK REPORT =====")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


def available_stock():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products WHERE Stock > 0")

    print("\n===== AVAILABLE STOCK REPORT =====")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()




def sales_report():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sales")

    print("\n===== SALES REPORT =====")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


def daily_sales():
    date = input("Enter Date (YYYY-MM-DD): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sales WHERE Sale_Date=%s", (date,))

    print("\n===== DAILY SALES =====")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


def monthly_sales():
    month = input("Enter Month (1-12): ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Sales WHERE MONTH(Sale_Date)=%s", (month,))

    print("\n===== MONTHLY SALES =====")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()


def product_pdf():
    print("Product Report PDF Generated Successfully")


def inventory_pdf():
    print("Inventory Report PDF Generated Successfully")


def sales_pdf():
    print("Sales Report PDF Generated Successfully")


while True:

    print("\n========== REPORTS ==========")
    print("1. View All Products")
    print("2. Search Product")
    print("3. Product Details")
    print("4. Low Stock Report")
    print("5. Out Of Stock Report")
    print("6. Available Stock Report")
    print("7. Sales Report")
    print("8. Daily Sales Report")
    print("9. Monthly Sales Report")
    print("10. Product PDF")
    print("11. Inventory PDF")
    print("12. Sales PDF")
    print("13. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        view_all_products()

    elif choice == "2":
        search_product()

    elif choice == "3":
        product_details()

    elif choice == "4":
        low_stock()

    elif choice == "5":
        out_of_stock()

    elif choice == "6":
        available_stock()

    elif choice == "7":
        sales_report()

    elif choice == "8":
        daily_sales()

    elif choice == "9":
        monthly_sales()

    elif choice == "10":
        product_pdf()

    elif choice == "11":
        inventory_pdf()

    elif choice == "12":
        sales_pdf()

    elif choice == "13":
        print("Thank You")
        break1

    else:
        print("Invalid Choice")
