import socket

def get(path, port):
    """ Just makes a GET request and prints the header """

    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    connection_path = ('localhost', port)
    server = socket.socket()
    server.connect( connection_path)
    server.send( request.encode())

    some_chunks = list()
    while True:
        chunk = server.recv(100) # This is blockig, so either gets chunks or whaits for
                                 # connection to be broken.
        if chunk:
            some_chunks.append( chunk)
        else:
            body = (b''.join(some_chunks)).decode() # Once the connection is broke, 
            print(body.split('\n')[0])              # we can end put all together and end.
            return 

def run(request_to_do):
    """ Takes a number and makes so many request"""

    path = '/'
    port = 5000

    request_number = 0 
    while request_to_do:
        print('request number ' + str(request_number))
        get(path, port)
        print('---------------\n')

        request_number += 1
        request_to_do -= 1 
