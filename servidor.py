import socket
from datetime import datetime
from database import crear_db, guardar_mensaje

HOST = "127.0.0.1"
PORT = 5000

def iniciar_servidor():
    print("INICIANDO SERVIDOR...")

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print("Servidor escuchando en puerto", PORT)
    except Exception as e:
        print("Error al iniciar servidor:", e)
        return None

    return servidor


def manejar_conexiones(servidor):
    print("Esperando conexiones...")

    while True:
        cliente, direccion = servidor.accept()
        print("Cliente conectado:", direccion)

        try:
            mensaje = cliente.recv(1024).decode()
            print("Mensaje recibido:", mensaje)

            if mensaje:
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Guardar en la base de datos
                guardar_mensaje(mensaje, fecha, direccion[0])

                # Responder al cliente
                respuesta = f"Mensaje recibido: {fecha}"
                cliente.send(respuesta.encode())

        except Exception as e:
            print("Error:", e)

        finally:
            cliente.close()


if __name__ == "__main__":
    print("EJECUTANDO MAIN...")
    crear_db()
    servidor = iniciar_servidor()

    if servidor:
        manejar_conexiones(servidor)