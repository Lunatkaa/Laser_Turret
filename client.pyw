import tkinter
import time
import socket

HOST = '10.25.208.42'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def handle_mouse(mouseposition):
    coordinate_label['text'] = f'{mouseposition.x},{mouseposition.y}'
    client.send(
        f'{int(180 - mouseposition.x / (root.winfo_width() / 180))}, {int(mouseposition.y / (root.winfo_height() / 180))}'.encode('ascii'))
    time.sleep(0.05)


root = tkinter.Tk()
root.title('LaserTurret')
root.geometry('1000x1000')
root.resizable(width=False, height=False)
root.configure(bg='#2E2E2E')
root.bind('<B1-Motion>', handle_mouse)

coordinate_label = tkinter.Label(
    root, text='???,???', bg='#2E2E2E', fg='white', font='Arial')
coordinate_label.grid(row=0, column=0)


root.mainloop()
