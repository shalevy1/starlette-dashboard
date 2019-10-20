# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .functions import call_api

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


@app.route("/{page}")
async def example_pages(request):
    try:
        html_page = request.path_params["page"]
        logger.info(f"page accessed: /example/{html_page}")

        if html_page == "tables-data":
            obj = call_api()
            context = {"request": request, "obj": obj}
        else:
            context = {"request": request}

        template = f"/pages/{html_page}.html"

        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(e)
