#!/usr/bin/env python3

import socket
import random


HOST = '127.0.0.1'
PORT = 5099

value = ((random.randint(1, 100)))
print(value)


message = f'Random value is: {value}'
print(message)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    s.sendall(message.encode())

    data = s.recv(1024)

    print('Received ', repr(data))
