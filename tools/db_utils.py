import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            cursor_factory=RealDictCursor,
        )
        return conn
    except Exception as e:
        print("❌ Error al conectar con PostgreSQL:", e)
        return None

def create_logs_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS logs (
                    id SERIAL PRIMARY KEY,
                    sensor VARCHAR(50),
                    value FLOAT,
                    timestamp TIMESTAMP DEFAULT now()
                )
            """)
        conn.commit()
        print("✅ Tabla `logs` lista.")
    except Exception as e:
        print("❌ Error al crear tabla:", e)
        conn.rollback()

def insert_log(conn, sensor, value):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO logs (sensor, value) VALUES (%s, %s)",
                (sensor, value)
            )
        conn.commit()
    except Exception as e:
        print(f"❌ Error al insertar log [{sensor}]:", e)
        check_logs_columns(conn)
        conn.rollback()

def check_logs_columns(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'logs'")
        cols = [row[0] for row in cur.fetchall()]
        expected = {'id', 'sensor', 'value', 'timestamp'}
        if not expected.issubset(set(cols)):
            print(f"⚠️ Columnas inesperadas: {set(cols)}")
        else:
            print("✅ Columnas de `logs` correctas.")
