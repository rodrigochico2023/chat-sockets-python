import sqlite3

def crear_db():
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mensajes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        contenido TEXT,
        fecha_envio TEXT,
        ip_cliente TEXT
    )
    """)

    conn.commit()
    conn.close()


def guardar_mensaje(contenido, fecha, ip):
    conn = sqlite3.connect("mensajes.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO mensajes (contenido, fecha_envio, ip_cliente)
    VALUES (?, ?, ?)
    """, (contenido, fecha, ip))

    conn.commit()
    conn.close()