# -*- coding: utf-8 -*-
from starlette.applications import Starlette

from .public_routes import app as public_routes

page_routes = Starlette()

# route to different endponts (public/private)
page_routes.mount("/", app=public_routes)
