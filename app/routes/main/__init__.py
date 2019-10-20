# -*- coding: utf-8 -*-
from starlette.applications import Starlette

from .main import app as main_routes

start_routes = Starlette()

start_routes.mount("/", app=main_routes)
