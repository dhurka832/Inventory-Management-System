from inventory import *

def menu():
    while True:
        print("\n" + "="*40)
        print("📦 Inventory Management System")
        print("="*40)
        print("1. Add Category")
        print("2. View Categories")
        print("3. Add Product")
        print("4. View Products")
        print("5. Update Product")
        print("6. Delete Product")
        print("7. Generate Invoice")
        print("8. Low Stock Alert")
        print("9. Exit")
        print("="*40)

        choice = input("Enter choice (1-9): ").strip()

        if choice == "1":
            name = input("Enter Category Name: ").strip()
            if name:
                add_category(name)
            else:
                print("Category name cannot be empty.")

        elif choice == "2":
            view_categories()

        elif choice == "3":
            try:
                name = input("Enter Product Name: ").strip()
                quantity = int(input("Enter Quantity: "))
                price = float(input("Enter Price: "))
                supplier = input("Enter Supplier Name: ").strip()
                category_id = int(input("Enter Category ID: "))
                add_product(name, quantity, price, supplier, category_id)
            except ValueError:
                print("Invalid input! Quantity, Price and Category ID must be numbers.")

        elif choice == "4":
            view_products()

        elif choice == "5":
            try:
                product_id = int(input("Enter Product ID to update: "))
                quantity = int(input("Enter New Quantity: "))
                price = float(input("Enter New Price: "))
                update_product(product_id, quantity, price)
            except ValueError:
                print("Invalid input! Product ID, Quantity and Price must be numbers.")

        elif choice == "6":
            try:
                product_id = int(input("Enter Product ID to delete: "))
                delete_product(product_id)
            except ValueError:
                print("Invalid input! Product ID must be a number.")

        elif choice == "7":
            try:
                product_id = int(input("Enter Product ID for invoice: "))
                quantity_sold = int(input("Enter Quantity Sold: "))
                generate_invoice(product_id, quantity_sold)
            except ValueError:
                print("Invalid input! Product ID and Quantity must be numbers.")

        elif choice == "8":
            try:
                threshold = input("Enter low stock threshold (default 5): ").strip()
                threshold = int(threshold) if threshold else 5
                low_stock_alert(threshold)
            except ValueError:
                print("Invalid threshold! Must be a number.")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter a number between 1-9.")

if __name__ == "__main__":
    menu()
