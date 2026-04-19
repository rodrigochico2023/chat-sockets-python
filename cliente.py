import socket

HOST = "127.0.0.1"
PORT = 5000

def iniciar_cliente():
    while True:
        mensaje = input("Escribí un mensaje ('éxito' para salir): ")

        if mensaje.lower() == "éxito":
            print("Finalizando cliente...")
            break

        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.connect((HOST, PORT))

            cliente.send(mensaje.encode())

            respuesta = cliente.recv(1024).decode()
            print("Servidor:", respuesta)

            cliente.close()

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    iniciar_cliente()