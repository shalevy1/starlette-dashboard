# -*- coding: utf-8 -*-
from starlette.applications import Starlette
from starlette.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    StreamingResponse,
)
from starlette.routing import Mount, Route, Router

from .main import app as main_routes

# from .private_routes import app as private_routes

start_routes = Starlette()

# page_routes.mount('/{user_id:int}', app=private_routes)
start_routes.mount("/", app=main_routes)
