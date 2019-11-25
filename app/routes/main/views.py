# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# from com_lib.file_functions import open_json

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


async def homepage(request):
    
    try:
        template = "index.html"
        context = {"request": request}
        logger.info(f"page accessed: /")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.info(f"Error: Page accessed: / , but error of {e} occurred")

async def homepage_page(request):
    try:
        html_page = request.path_params["page"]
        template = f"{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.info(f"Error: Page accessed: {template}, but error of {e} occurred")
