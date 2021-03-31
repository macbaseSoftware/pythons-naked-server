from aiohttp import web
import socketio

#create a new async socket io server
sio = socketio.AsyncServer()

#create a new aiohttp web server
app = web.Application()

#bind the socketio server to the web application:
sio.attach(app)


#aiHttp endpoing normally...
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
@sio.on('message')
async def print_message(sid, message):
    # When we receive a new event of type
    # 'message' through a socket.io connection
    # we print the socket ID and the message
    print("Socket ID: " , sid)
    print(message)
    await sio.emit('message', "From server: "+message)


# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)

          # app.run(host='0.0.0.0', port=80)