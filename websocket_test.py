# -*- coding: utf-8 -*-

from bottle import request, Bottle, abort
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler

app = Bottle()


@app.route('/websocket')
def handle_websocket():
    print("===================")
    wsock = request.environ.get('wsgi.websocket')
    print(request['route.url_args'])
    print(wsock)
    print(type(wsock))
    if not wsock:
        abort(400, 'Expected WebSocket request.')
    while True:
        try:
            message = wsock.receive()
            wsock.send("Your message was: %r" % message)
        except WebSocketError:
            break

server = WSGIServer(("0.0.0.0", 5000), app, handler_class=WebSocketHandler)
server.serve_forever()
