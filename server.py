import serial
import socket

serial_connection = serial.Serial(port='COM5', baudrate=9600)

HOST = 'raspberrypi'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

client, addr = server.accept()
print(f'{addr} Connected')


def receive():
    while True:
        try:
            coordinates = server.recv(1024)
            serial_connection.write(coordinates)
