from tools.db_utils import get_db_connection  # ← Usa ruta completa si está en /tools

try:
    conn = get_db_connection()
    if conn is None:
        raise RuntimeError("Conexión fallida (None)")

    with conn.cursor() as cursor:
        cursor.execute("SELECT 1;")
        print("PostgreSQL conectado correctamente.")

except Exception as e:
    print("Error al conectar con PostgreSQL:")
    print(e)

finally:
    if conn:
        conn.close()



