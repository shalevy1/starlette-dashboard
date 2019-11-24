# -*- coding: utf-8 -*-
import uvicorn
from loguru import logger
from starlette.applications import Starlette
from starlette.config import Config
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from com_lib.logging_config import config_logging
from db_setup import create_db
from routes import routes

config = Config(".env")
logger.info("Logging initiated")

app_env = config("RELEASE_ENV", default="prd")

debug_mode = False

if app_env == "dev":
    debug_mode = True

# initialize logging
config_logging()
# create database
create_db()
logger.info("Databasee initiated")

app = Starlette(debug=True)
logger.info("Application initiated")

# templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")

# all routes for all pages
app.mount("/", routes)


@app.on_event("startup")
def startup():

    logger.info("Applicaton started")
    logger.info(f"Debug Mode set to {debug_mode}")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Applicaton shutdown")


@app.route("/error")
async def error(request):
    """
    An example error. Switch the `debug` setting to see either tracebacks or 500 pages.
    """
    raise RuntimeError("Oh no")


@app.exception_handler(403)
async def forbidden_403(request, exc):
    print(request, exc)
    """
    Return an HTTP 403 page.
    """
    template = "/error/403.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=403)


@app.exception_handler(404)
async def not_found_404(request, exc):
    print(request, exc)
    """
    Return an HTTP 404 page.
    """
    template = "/error/404.html"
    context = {"request": request}
    return templates.TemplateResponse(template, context, status_code=404)


@app.exception_handler(500)
async def server_error(request, exc):
    print(request, exc)
    """
    Return an HTTP 500 page.
    """
    template = "/error/500.html"
    context = {"request": request}
    logger.critical(context,exc)
    return templates.TemplateResponse(template, context, status_code=500)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")
