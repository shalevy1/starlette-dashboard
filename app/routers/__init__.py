# -*- coding: utf-8 -*-
from starlette.routing import Mount, Route, Router

from .users import users_routes
from .websocket import websockets_routes

# mounted app can also be an instance of `Router()`
routes = Router(
    [
        # Route('/', endpoint=Homepage, methods=['GET']),
        Mount("/users", app=users_routes),
        Mount("/public", app=websockets_routes),
    ]
)
