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
async def index(request):
    try:
        logger.info(f"page accessed: /index")
        template = "index.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.info(f"Error: Page accessed: / , but error of {e} occurred")

@app.route("/{page}")
async def homepage(request):
    try:
        html_page = request.path_params["page"]
        logger.info(f"page accessed: /{page}")
        template = f"{page}.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
    except Exception as e:
        # logger.critical(e)
        logger.info(f"Error: Page accessed: /{page}, but error of {e} occurred")
