from database.db import get_connection
from services.catalog_service import get_product

def add_to_cart(user_id: int, product_id: int, quantity: int = 1):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO cart (user_id, product_id, quantity)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id, product_id) DO UPDATE SET quantity = quantity + ?
        """, (user_id, product_id, quantity, quantity))
        conn.commit()

def get_cart(user_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, quantity FROM cart WHERE user_id = ?", (user_id,))
        items = cursor.fetchall()
        return [
            {"product": get_product(pid), "quantity": qty}
            for pid, qty in items
        ]

def clear_cart(user_id: int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cart WHERE user_id = ?", (user_id,))
        conn.commit()

def calculate_total(cart_items: list):
    return sum(item["product"]["price"] * item["quantity"] for item in cart_items)
