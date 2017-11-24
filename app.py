# -*- coding: utf-8 -*-

import bottle
import canister
from bottle import request, response, route, run, Bottle

app = Bottle()
app.config.load_config('config.config')
app.install(canister.Canister())


@app.route('/')
def index():
    app.log.debug('Some debug message')
    app.log.info('Some info message')
    app.log.warn('Some warning message')
    app.log.error('Some error message')
    app.log.critical('Big problem!')
    return {"test": "123"}

app.run(host="localhost", port=9000)
