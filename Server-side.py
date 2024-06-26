import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address, file=sys.stderr)

        while True:
            data = connection.recv(16)
            print('received "%s"' % data.decode(), file=sys.stderr)
            if data:
                print('sending data back to the client', file=sys.stderr)
                connection.sendall(data)
            else:
                print('no more data from', client_address, file=sys.stderr)
                break

    finally:
        connection.close()
