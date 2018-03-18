# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 20:29:01 2018

@author: 28148
"""

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body = b'Awsome 嘿嘿')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()