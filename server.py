import select
import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 50000))
server.listen(5)

inputs = [server]
outputs = []

while inputs:
    readable, writable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            inputs.append(connection)
            print(f"New connection from {client_address}")
        else:
            data = s.recv(1024)
            if data:
                print(f"received '{data}' from {s.getpeername()}")
                if s not in outputs:
                    outputs.append(s)
            else:
                print(f"closing connection to {s.getpeername()}")
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

    for s in writable:
        s.send(b"Hello, client!")
        outputs.remove(s)

    for s in exceptional:
        print(f"handling exceptional condition for {s.getpeername()}")
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
