from database.db import get_connection
from aiogram.types import User

def create_user(user: User):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR IGNORE INTO users (telegram_id, full_name) VALUES (?, ?)",
            (user.id, user.full_name)
        )
        conn.commit()

def get_user_balance(user_id: int) -> float | None:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT balance FROM users WHERE telegram_id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        return row[0] if row else None
    
def update_user_balance(user_id: int, amount: float):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE users SET balance = balance + ? WHERE telegram_id = ?",
            (amount, user_id)
        )
        conn.commit()

