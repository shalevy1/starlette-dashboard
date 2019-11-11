# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# from com_lib.file_functions import open_json

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


# @app.route("/")
async def homepage(request):
    print('hi')
    try:
        # html_page = request.path_params["page"]
        logger.info(f"page accessed: /")
        template = "index.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.info(f"Error: Page accessed: / , but error of {e} occurred")

# @app.route("/{page}")
async def homepage_page(request):
    print('hi')
    try:
        html_page = request.path_params["page"]
        logger.info(f"page accessed: /{html_page}")
        template = f"{html_page}.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.info(f"Error: Page accessed: /{html_page}, but error of {e} occurred")
