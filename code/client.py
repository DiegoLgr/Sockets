import socket
import time


def get(path, port):


    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    connection_path = ('localhost', port)
    server = socket.socket()
    server.connect( connection_path)
    server.send( request.encode())

    some_chunks = list()
    while True:
        chunk = server.recv(1000)
        if chunk:
            some_chunks.append( chunk)
        else:
            body = (b''.join(some_chunks)).decode()
            print(body.split('\n')[0])
            return 1
