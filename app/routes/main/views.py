# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


async def homepage(request):

    template = "index.html"
    context = {"request": request}
    logger.info(f"page accessed: /")
    return templates.TemplateResponse(template, context)


async def homepage_page(request):
    try:
        html_page = request.path_params["page"]
        template = f"{html_page}.html"
        context = {"request": request}
        logger.info(f"page accessed: {template}")
        return templates.TemplateResponse(template, context)

    except Exception as e:
        logger.critical(
            f"Error: Page accessed: /{html_page} , but HTML page {e} does not exist"
        )
        raise HTTPException(404, detail="page note found")
