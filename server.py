import serial
import socket
import time

serial_connection = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

HOST = 'raspberrypi'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print(f'[SERVER] Server is listening on {HOST}:{PORT}')


def main():
    while True:
        client, addr = server.accept()
        print(f'[CONNECTION] {str(addr)} Connected')
        receive(client)


def receive(client):
    while True:
        try:
            coordinates = client.recv(1024)
            serial_connection.write(coordinates)
            print(coordinates)
            time.sleep(0.05)
        except:
            print('[ERROR]something went wrong! shuting down now')
            break


main()
