from aiohttp import web
import socketio

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# creates a new Aiohttp web Application
app = web.Application()
# binds our Socket.IO server to our App
# instance
sio.attach(app)

# we can define aiohttp endpoints just as we normally
# would with no changes
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# if we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
@sio.on('message')
async def print_message(sid, message):
    # when we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print('Socket ID: ', sid)
    print(message)
    # await a successful emit o our reversed message
    # back to the client
    await sio.emit('message', message[::-1])

# we bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# we kick off our server
if __name__=='__main__':
    web.run_app(app)