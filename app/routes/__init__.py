# -*- coding: utf-8 -*-
from starlette.routing import Mount, Route, Router
from .main import start_routes
from .pages import page_routes

# mounted app can also be an instance of `Router()`
routes = Router(
    [
        Route("/", endpoint=start_routes, methods=["GET"]),
        # Mount("/", app=start_routes),
        Mount("/pages", app=page_routes),
        # Mount("/public", app=websockets_routes),
    ]
)
