# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .functions import call_api

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


async def homepage(request):
    try:
        # html_page = request.path_params["page"]
        logger.info(f"page accessed: /pages")
        template = f"index.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(f"Error: Page accessed: / , but error of {e} occurred")


async def example_pages(request):
    html_page = request.path_params["page"]
    try:
        template = f"/pages/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(f"Error: Page accessed: {template}, but error of {e} occurred")

async def example_pages_charts(request):
    html_page = request.path_params["page"]
    try:
        # html_page = request.path_params["page"]
        
        template = f"/pages/charts/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.critical(f"Error: Page accessed: {template}, but error of {e} occurred")

async def example_pages_forms(request):
    html_page = request.path_params["page"]
    logger.info(f"page requested: {html_page}")
    try:
        # html_page = request.path_params["page"]
        
        template = f"/pages/forms/{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.critical(f"Error: Page accessed: {template}, but error of {e} occurred")
