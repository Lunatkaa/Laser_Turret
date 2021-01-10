import tkinter
import time
import socket

HOST = 'raspberrypi'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


root = tkinter.Tk()
root.title('LaserTurret')
root.geometry('1000x1000')
root.resizable(width=False, height=False)
root.configure(bg='#2E2E2E')
root.bind('<B1-Motion>', handle_mouse)

coordinate_label = tkinter.Label(
    root, text='???,???', bg='#2E2E2E', fg='white')
coordinate_label.grid(row=0, column=0)


def handle_mouse(mouseposition):
    coordinate_label['text'] = f'{mouseposition.x},{mouseposition.y}'
    client.send(f'{mouseposition.x}, {mouseposition.y}')
    time.sleep(0.05)


root.mainloop()
