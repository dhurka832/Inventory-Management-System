from db_config import get_connection
from prettytable import PrettyTable


def add_category(name):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "INSERT INTO categories (category_name) VALUES (%s)"
        cursor.execute(query, (name,))
        conn.commit()
        print("Category added successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def view_categories():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM categories")
        records = cursor.fetchall()
        if not records:
            print("No categories found.")
            return

        table = PrettyTable()
        table.field_names = ["Category ID", "Category Name"]
        for row in records:
            table.add_row([row[0], row[1]])
        print("\nCategories:")
        print(table)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def add_product(name, quantity, price, supplier, category_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = """
        INSERT INTO products (name, quantity, price, supplier, category_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, quantity, price, supplier, category_id))
        conn.commit()
        print("Product added successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def view_products():
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = """
        SELECT p.product_id, p.name, p.quantity, p.price, p.supplier, c.category_name
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.category_id
        """
        cursor.execute(query)
        records = cursor.fetchall()
        if not records:
            print("No products found.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Name", "Qty", "Price", "Supplier", "Category"]
        for row in records:
            table.add_row(row)
        print("\nInventory List:")
        print(table)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def update_product(product_id, quantity, price):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        query = "UPDATE products SET quantity=%s, price=%s WHERE product_id=%s"
        cursor.execute(query, (quantity, price, product_id))
        conn.commit()
        if cursor.rowcount:
            print("Product updated successfully!")
        else:
            print("Product not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def delete_product(product_id):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM products WHERE product_id=%s", (product_id,))
        conn.commit()
        if cursor.rowcount:
            print("Product deleted successfully!")
        else:
            print("Product not found.")
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def generate_invoice(product_id, quantity_sold):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT name, price, quantity FROM products WHERE product_id=%s", (product_id,))
        product = cursor.fetchone()

        if not product:
            print("Product not found!")
            return

        name, price, available_quantity = product

        if quantity_sold > available_quantity:
            print("Not enough stock available!")
            return

        total_amount = price * quantity_sold

        cursor.execute(
            "INSERT INTO invoices (product_id, quantity_sold, total_amount) VALUES (%s, %s, %s)",
            (product_id, quantity_sold, total_amount)
        )
        cursor.execute(
            "UPDATE products SET quantity = quantity - %s WHERE product_id = %s",
            (quantity_sold, product_id)
        )
        conn.commit()

        table = PrettyTable()
        table.field_names = ["Product ID", "Product Name", "Quantity Sold", "Price per Unit", "Total Amount"]
        table.add_row([product_id, name, quantity_sold, price, total_amount])
        print("\nInvoice Generated Successfully")
        print(table)

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


def low_stock_alert(threshold=5):
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT product_id, name, quantity FROM products WHERE quantity <= %s",
            (threshold,)
        )
        records = cursor.fetchall()

        print("\nLow Stock Products:")
        if not records:
            print("All products have sufficient stock.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Product Name", "Quantity"]
        for row in records:
            table.add_row(row)
        print(table)
    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()
