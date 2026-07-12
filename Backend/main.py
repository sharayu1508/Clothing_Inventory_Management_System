from login import login
from supplier import supplier_menu
from product import view_product
from product import product_menu
from inventory import inventory_menu
from sales import sales_menu
from reports import reports_menu

def admin_menu():
    while True:
        print("\n===== CLOTHING INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Supplier Management")
        print("2. Product Management")
        print("3. Inventory Management")
        print("4. Sales Management")
        print("5. Reports")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            supplier_menu()

        elif choice == "2":
            product_menu()

        elif choice == "3":
            inventory_menu()

        elif choice == "4":
            sales_menu()

        elif choice == "5":
            reports_menu()

        elif choice == "6":
            print("Logged Out Successfully...")
            break

        else:
            print("Invalid Choice!")


def user_menu():
    while True:
        print("\n===== Customer MENU =====")
        print("1. View Products")
        print("2. Purchase Product")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_product()

        elif choice == "2":
            sales_menu()

        elif choice == "3":
            sales_menu()

        elif choice == "4":
            print("Logged Out Successfully...")
            break

        else:
            print("Invalid Choice!")


def main():
    role = login()

    if role == "admin":
        admin_menu()

    elif role == "user":
        user_menu()

    else:
        print("Login Failed...")


if __name__ == "__main__":
    main()
