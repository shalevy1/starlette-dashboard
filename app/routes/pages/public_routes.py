import requests
from loguru import logger
from starlette.applications import Starlette
from starlette.authentication import requires
from starlette.responses import (FileResponse, HTMLResponse, JSONResponse,
                                 PlainTextResponse, RedirectResponse,
                                 StreamingResponse)
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from com_lib.file_functions import open_json

from .functions import call_api

# from models import *

app = Starlette()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="statics"), name="static")


# @app.route("/")
# @app.route("/index")
# async def homepage(request):
#     try:
#         logger.info(f"page accessed: /")
#         template = "index.html"
#         context = {"request": request}
#         return templates.TemplateResponse(template, context)
#     except HTTPException as e:
#         logger.critical(e)


@app.route("/login")
async def login(request):
    try:
        # html_page = request.path_params["page"]
        logger.info(f"page accessed: login")

        context = {"request": request}

        template = f"login.html"
        return templates.TemplateResponse(template, context)
    except HTTPException as e:
        logger.critical(e)


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


# @app.route('/')     # methods defaults to GET
# # protected endpoint, any authorized user can access it
# @requires('user_auth')
# async def users(request):
#     query = users_table.select()
#     results = await database.fetch_all(query)
#     content = [
#         {
#             "name": result["name"],
#         }
#         for result in results
#     ]
#     return JSONResponse(content)


# @app.route("/login", methods=["POST"])
# async def login_user(request):
#     # redirect to previous path (aquired from session cookie) after login
#     if 'history' in request.session and len(request.session['history']):
#         previous = request.session['history'].pop()
#     else:
#         previous = '/'

#     # request.form() requieres python-multipart as dependency
#     form = await request.form()
#     username = form["name"]
#     password = form["password"]
#     query = users_table.select().where(users_table.c.name == username)
#     try:
#         results = await database.fetch_one(query)
#     except:
#         return RedirectResponse(previous)
#     hashed_pass = results['hashed']

#     valid_pass = await check_password(form["password"], hashed_pass)

#     response = RedirectResponse(previous)
#     if valid_pass:
#         response.set_cookie('jwt', generate_jwt(results['id']), httponly=True)
#     return response


# @app.route("/", methods=["POST"])
# async def new_user(request):
#     # request.form() requieres python-multipart as dependency
#     form = await request.form()
#     password = form["password"]
#     hashed_pass = await get_hashed_password(password)
#     query = users_table.insert().values(
#         name=form["name"],
#         hashed=hashed_pass,
#     )
#     await database.execute(query)
#     return JSONResponse({
#         "name": form["name"],
#     }, status_code=201)
