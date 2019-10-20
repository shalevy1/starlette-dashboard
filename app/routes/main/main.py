# -*- coding: utf-8 -*-
from loguru import logger
from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# from com_lib.file_functions import open_json

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


@app.route("/")
@app.route("/index")
async def homepage(request):
    try:
        logger.info(f"page accessed: /")
        template = "index.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except Exception as e:
        logger.critical(e)
