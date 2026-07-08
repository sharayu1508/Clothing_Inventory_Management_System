from database import get_connection

class Product:

    # -------------------- ADD PRODUCT --------------------

    def add_product(self):

        conn = get_connection()
        cursor = conn.cursor()

        product_name = input("Enter Product Name : ")
        category = input("Enter Category : ")
        brand = input("Enter Brand : ")
        size = input("Enter Size : ")
        color = input("Enter Color : ")
        selling_price = float(input("Enter Selling Price : "))
        stock = int(input("Enter Stock : "))
        supplier_id = int(input("Enter Supplier ID : "))

        cursor.execute(
            "SELECT Supplier_ID FROM Suppliers WHERE Supplier_ID=%s",
            (supplier_id,)
        )

        if cursor.fetchone() is None:
            print("Supplier ID does not exist.")
            cursor.close()
            conn.close()
            return

        sql = """
        INSERT INTO Products
        (Product_Name, Category, Brand, Size, Color,
        Selling_Price, Stock, Supplier_ID)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            product_name,
            category,
            brand,
            size,
            color,
            selling_price,
            stock,
            supplier_id
        )

        cursor.execute(sql, values)
        conn.commit()

        print("Product Added Successfully.")

        cursor.close()
        conn.close()

    # -------------------- VIEW PRODUCT --------------------

    def view_product(self):

        conn = get_connection()
        cursor = conn.cursor()

        while True:

            print("\n========== VIEW PRODUCT ==========")
            print("1. View All Products")
            print("2. View Product Details")
            print("3. Refresh Product List")
            print("4. Back")

            choice = input("Enter Your Choice : ")

            if choice == "1":

                cursor.execute("""
                SELECT Product_ID, Product_Name, Category,
                Brand, Size, Color,
                Selling_Price, Stock, Supplier_ID
                FROM Products
                """)

                products = cursor.fetchall()

                if products:
                    print("\n------ PRODUCT LIST ------")
                    for product in products:
                        print(product)
                else:
                    print("No Products Found.")

            elif choice == "2":

                product_id = int(input("Enter Product ID : "))

                cursor.execute("""
                SELECT Product_ID, Product_Name, Category,
                Brand, Size, Color,
                Selling_Price, Stock, Supplier_ID
                FROM Products
                WHERE Product_ID=%s
                """, (product_id,))

                product = cursor.fetchone()

                if product:

                    print("\n------ PRODUCT DETAILS ------")
                    print("Product ID :", product[0])
                    print("Product Name :", product[1])
                    print("Category :", product[2])
                    print("Brand :", product[3])
                    print("Size :", product[4])
                    print("Color :", product[5])
                    print("Selling Price :", product[6])
                    print("Stock :", product[7])
                    print("Supplier ID :", product[8])

                else:
                    print("Product Not Found.")

            elif choice == "3":

                print("\nRefreshing Product List...\n")

                cursor.execute("""
                SELECT Product_ID, Product_Name, Category,
                Brand, Size, Color,
                Selling_Price, Stock, Supplier_ID
                FROM Products
                """)

                products = cursor.fetchall()

                if products:
                    for product in products:
                        print(product)
                else:
                    print("No Products Found.")

            elif choice == "4":
                break

            else:
                print("Invalid Choice!")

        cursor.close()
        conn.close()


        # -------------------- UPDATE PRODUCT --------------------

    def update_product(self):

        conn = get_connection()
        cursor = conn.cursor()

        product_id = int(input("Enter Product ID : "))

        cursor.execute(
            "SELECT * FROM Products WHERE Product_ID=%s",
            (product_id,)
        )

        if cursor.fetchone() is None:
            print("Product Not Found")
            cursor.close()
            conn.close()
            return

        while True:

            print("\n========== UPDATE PRODUCT ==========")
            print("1. Update Product Name")
            print("2. Update Category")
            print("3. Update Brand")
            print("4. Update Size")
            print("5. Update Color")
            print("6. Update Purchase Price")
            print("7. Update Selling Price")
            print("8. Update Stock")
            print("9. Update Supplier ID")
            print("10. Save and Exit")

            choice = int(input("Enter Choice : "))

            if choice == 1:
                value = input("New Product Name : ")
                cursor.execute(
                    "UPDATE Products SET Product_Name=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 2:
                value = input("New Category : ")
                cursor.execute(
                    "UPDATE Products SET Category=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 3:
                value = input("New Brand : ")
                cursor.execute(
                    "UPDATE Products SET Brand=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 4:
                value = input("New Size : ")
                cursor.execute(
                    "UPDATE Products SET Size=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 5:
                value = input("New Color : ")
                cursor.execute(
                    "UPDATE Products SET Color=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 6:
                value = float(input("New Purchase Price : "))
                cursor.execute(
                    "UPDATE Products SET Purchase_Price=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 7:
                value = float(input("New Selling Price : "))
                cursor.execute(
                    "UPDATE Products SET Selling_Price=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 8:
                value = int(input("New Stock : "))
                cursor.execute(
                    "UPDATE Products SET Stock=%s WHERE Product_ID=%s",
                    (value, product_id)
                )

            elif choice == 9:
                supplier = int(input("New Supplier ID : "))

                cursor.execute(
                    "SELECT Supplier_ID FROM Suppliers WHERE Supplier_ID=%s",
                    (supplier,)
                )

                if cursor.fetchone() is None:
                    print("Supplier ID Not Found")
                    continue

                cursor.execute(
                    "UPDATE Products SET Supplier_ID=%s WHERE Product_ID=%s",
                    (supplier, product_id)
                )

            elif choice == 10:
                conn.commit()
                print("Product Updated Successfully.")
                break

            else:
                print("Invalid Choice")

        cursor.close()
        conn.close()

   
        # -------------------- DELETE PRODUCT --------------------

    def delete_product(self):

        conn = get_connection()
        cursor = conn.cursor()

        # 1.5.1 Delete by Product ID
        product_id = int(input("Enter Product ID to Delete : "))

        cursor.execute(
            "SELECT * FROM Products WHERE Product_ID=%s",
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:
            print("Product Not Found.")
            cursor.close()
            conn.close()
            return

        print("\nProduct Details")
        print(product)

        # 1.5.2 Confirm Product Deletion
        confirm = input("Are you sure you want to delete this product? (Y/N): ")

        if confirm.upper() == "Y":

            # 1.5.3 Remove Product from Database
            cursor.execute(
                "DELETE FROM Products WHERE Product_ID=%s",
                (product_id,)
            )

            conn.commit()
            print("Product Deleted Successfully.")

        else:
            print("Delete Cancelled.")

        cursor.close()
        conn.close()
            # -------------------- SEARCH PRODUCT --------------------

    def search_product(self):

        conn = get_connection()
        cursor = conn.cursor()

        while True:

            print("\n========== SEARCH PRODUCT ==========")
            print("1. Search by Product ID")
            print("2. Search by Product Name")
            print("3. Search by Category")
            print("4. Search by Brand")
            print("5. Search by Size")
            print("6. Search by Color")
            print("7. Search by Purchase Price")
            print("8. Search by Selling Price")
            print("9. Search by Stock")
            print("10. Search by Supplier ID")
            print("11. Back")

            choice = int(input("Enter Choice : "))

            if choice == 1:
                field = "Product_ID"
                value = input("Enter Product ID : ")
                sql = f"SELECT * FROM Products WHERE {field}=%s"

            elif choice == 2:
                field = "Product_Name"
                value = "%" + input("Enter Product Name : ") + "%"
                sql = f"SELECT * FROM Products WHERE {field} LIKE %s"

            elif choice == 3:
                field = "Category"
                value = "%" + input("Enter Category : ") + "%"
                sql = f"SELECT * FROM Products WHERE {field} LIKE %s"

            elif choice == 4:
                field = "Brand"
                value = "%" + input("Enter Brand : ") + "%"
                sql = f"SELECT * FROM Products WHERE {field} LIKE %s"

            elif choice == 5:
                field = "Size"
                value = "%" + input("Enter Size : ") + "%"
                sql = f"SELECT * FROM Products WHERE {field} LIKE %s"

            elif choice == 6:
                field = "Color"
                value = "%" + input("Enter Color : ") + "%"
                sql = f"SELECT * FROM Products WHERE {field} LIKE %s"

            elif choice == 7:
                field = "Purchase_Price"
                value = float(input("Enter Purchase Price : "))
                sql = f"SELECT * FROM Products WHERE {field}=%s"

            elif choice == 8:
                field = "Selling_Price"
                value = float(input("Enter Selling Price : "))
                sql = f"SELECT * FROM Products WHERE {field}=%s"

            elif choice == 9:
                field = "Stock"
                value = int(input("Enter Stock : "))
                sql = f"SELECT * FROM Products WHERE {field}=%s"

            elif choice == 10:
                field = "Supplier_ID"
                value = int(input("Enter Supplier ID : "))
                sql = f"SELECT * FROM Products WHERE {field}=%s"

            elif choice == 11:
                break

            else:
                print("Invalid Choice")
                continue

        cursor.execute(sql, (value,))
        products = cursor.fetchall()

        if products:
            print("\n------ SEARCH RESULT ------")
            for product in products:
                print(product)
        else:
            print("No Product Found.")

        cursor.close()
        conn.close()
    
    # -------------------- PRODUCT MENU --------------------

    def menu(self):
  
        while True:

            print("\n========== PRODUCT MODULE ==========")
            print("1. Add Product")
            print("2. View Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Search Product")
            print("6. Exit")

            try:

                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    self.add_product()

                elif choice == 2:
                    self.view_product()

                elif choice == 3:
                    self.update_product()

                elif choice == 4:
                    self.delete_product()

                elif choice == 5:
                    self.search_product()

                elif choice == 6:
                    print("Thank You!")
                    

                else:
                    print("Invalid Choice!")

            except ValueError:
                print("Please Enter a Valid Number.")
if __name__ == "__main__":
    product = Product()
    product.menu()