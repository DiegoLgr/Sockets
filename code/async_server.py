import socket
import asyncio
from socket import AF_INET, SOCK_STREAM

async def runServer(loop):
    """ Makes the socket and waits for connections """

    connection = socket.socket(AF_INET, SOCK_STREAM)
    connection.bind(('', 5000))
    connection.listen(3)
    connection.setblocking(False)

    while True:
        client, addr = await loop.sock_accept(connection)
        print('Connection from', addr)
        loop.create_task(echo_handler(client, loop))

async def echo_handler(client, loop):
    """ Gets some data (the http request in this case), 
        simulates to make something slow and retuns a simple 
        message """

    while True:
        data = await loop.sock_recv(client, 1000)
        print('Recived : ' + data.decode())
        
        await asyncio.sleep(2) # Simulate some heavy work

        await loop.sock_sendall(client, b'Its working')
        break

    print('connection closed')
    client.close()

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(runServer(loop))

