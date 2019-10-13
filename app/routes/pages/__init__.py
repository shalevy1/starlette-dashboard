from starlette.applications import Starlette
from starlette.responses import (FileResponse, HTMLResponse, JSONResponse,
                                 PlainTextResponse, RedirectResponse,
                                 StreamingResponse)
from starlette.routing import Mount, Route, Router

from .public_routes import app as public_routes

# from .private_routes import app as private_routes

page_routes = Starlette()

# route to different endponts (public/private)
page_routes.mount("/", app=public_routes)
# page_routes.mount('/{user_id:int}', app=private_routes)
