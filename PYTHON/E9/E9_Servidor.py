import socket
from cryptography.fernet import Fernet
#parámetros de la conexión
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
HOST = 'localhost'
#estableciendo conexión
obj = socket.socket()
obj.bind((TCP_IP,TCP_PORT))
obj.listen()
conn, adrdress = obj.accept()
while True:
    msj = conn.recv(BUFFER_SIZE)
    respuesta = conn.send(b'Enterado. Bye!')
    break
obj.close()

#objeto de cifrado
file = open('.\clave.key', 'rb')
key = file.read()
file.close()
cipher_suite = Fernet(key)

#Descifrando mensaje
msj = cipher_suite.decrypt(msj, None)
msj = msj.decode()
print('Mensaje recibido: \n', msj)
