import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "users.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
