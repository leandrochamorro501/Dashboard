from pathlib import Path
import sqlite3

DATABASE_PATH = Path(__file__).resolve().parent / "data" / "monitor.sqlite"


def create_database():
    DATABASE_PATH.parent.mkdir(exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS measurements (
                id INTEGER PRIMARY KEY,
                measured_at_utc TEXT NOT NULL,
                cpu_percent REAL NOT NULL,
                ram_percent REAL NOT NULL,
                disk_percent REAL NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def save_sample(sample):
    connection = sqlite3.connect(DATABASE_PATH)
    try:
        connection.execute(
            """
            INSERT INTO measurements (
                measured_at_utc, cpu_percent, ram_percent, disk_percent
            ) VALUES (
                :measured_at_utc, :cpu_percent, :ram_percent, :disk_percent
            )
            """,
            sample,
        )
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    create_database()
    print("Database ready")