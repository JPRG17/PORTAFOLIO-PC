import argparse
import socket
from cryptography.fernet import Fernet as fernet

#Datos de conexión
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048
HOST = 'localhost'

#Parsing de argumentos
description = """ Modo de uso:
    E9_Cliente.py -msj 'Mensaje a enviar' """

parser = argparse.ArgumentParser(description='Port scanning',
                                 epilog=description)
parser.add_argument('-msj', help='Define el mensaje a enviar',
                    required=True, metavar='msj', dest='msj')
params = parser.parse_args()

#objeto de cifrado
key = fernet.generate_key()
cipher_suite = fernet(key)
file = open('.\clave.key', 'wb')
file.write(key)
file.close()

#convertir argumento
msj = params.msj
msj = msj.encode()

#cifrado de mensaje
msj = cipher_suite.encrypt(msj)
print('mensaje enviado: \n', params.msj)

#Establecer conexión
s = socket.socket()
s.connect((TCP_IP, TCP_PORT))
s.send(msj)
respuesta = s.recv(BUFFER_SIZE).decode()
s.close()

print('Respuesta recibida: ', respuesta)
