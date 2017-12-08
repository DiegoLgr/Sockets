import socket
import asyncio

async def connect():
    connection_path = ('localhost', 5000)
    try:
        server = socket.socket()
        server.connect( connection_path)
        server.setblocking(False)
    finally:
        print("Conectado")
        return server
    await asyncio.sleep(0)

async def get(future, path ):
    request = 'GET %s HTTP/1.0\r\n\r\n' % path
    server = await  connect()

    print("In the get function")

    try:
        server.send( request.encode())
    except:
        pass

    some_chunks = list()
    chunk = None
    while True:
        try:
            chunk = server.recv( 100) 
            print('pasando')         
            if chunk:
                some_chunks.append( chunk)
            else:
                body = (b''.join(some_chunks)).decode()
                print(body.split('\n')[0])      

                future.set_result("worked") 
            await asyncio.sleep(0)
        except:
            await asyncio.sleep(0)

def run(request_to_do):
    """ Takes a number and makes so many request"""
    request_number = 0
    path = '/'
    port = 5000

    asyncio.set_event_loop( asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    print("hola")
    asyncio.ensure_future( get( future, path))
    loop.run_until_complete(future)
    print("adios")
    loop.close()







if __name__=="__main__":
    run(1)











