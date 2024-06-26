import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
print('connecting to %s port %s' % server_address, file=sys.stderr)
sock.connect(server_address)

try:
    message = b'Repeat this message'  
    print('sending "%s"' % message, file=sys.stderr)
    sock.sendall(message)

    amount_received = 0  
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data, file=sys.stderr)

finally:
    print('closing socket', file=sys.stderr)
    sock.close()
