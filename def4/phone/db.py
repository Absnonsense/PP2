import psycopg2
from config import load_config
import csv
def connect():
    return psycopg2.connect(**load_config())
def create_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    phone VARCHAR(20) NOT NULL
                );
            """)
        conn.commit()
def insert_from_console(name, phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (name, phone))
        conn.commit()
def insert_from_csv(filename):
    with connect() as conn:
        with conn.cursor() as cur, open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (row[0], row[1]))
        conn.commit()
def update_user(name, new_name=None, new_phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute("UPDATE phonebook SET name = %s WHERE name = %s;", (new_name, name))
            if new_phone:
                cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s;", (new_phone, name))
        conn.commit()
def query_users(filter_name=None, filter_phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            query = "SELECT name, phone FROM phonebook WHERE TRUE"
            params = []
            if filter_name:
                query += " AND name ILIKE %s"
                params.append(f"%{filter_name}%")
            if filter_phone:
                query += " AND phone ILIKE %s"
                params.append(f"%{filter_phone}%")
            cur.execute(query, params)
            return cur.fetchall()
def delete_user(name=None, phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute("DELETE FROM phonebook WHERE name = %s;", (name,))
            if phone:
                cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
        conn.commit()
