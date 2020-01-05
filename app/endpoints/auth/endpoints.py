# -*- coding: utf-8 -*-
from loguru import logger

# from starlette.applications import Starlette
# from starlette.exceptions import HTTPException
# from starlette.staticfiles import StaticFiles
# from starlette.templating import Jinja2Templates
# from starlette.authentication import requires
# from app_functions import crud_ops, db_setup
# from starlette.responses import RedirectResponse
# from starlette.datastructures import URL
# from com_lib.pass_lib import verify_pass
# import base64


# async def login(request):

#     form = await request.form()
#     user_name = form["user_name"]
#     pwd = form["password"]
#     e_pwd = base64.encode(pwd)
#     query = (
#         db_setup.users.select()
#         .where(db_setup.users.c.user_name == user_name)
#         .order_by(db_setup.users.c.date_create)
#         .limit(qty)
#         .offset(offset)
#     )
#     user_info = await crud_ops.fetch_one_db(query=query)

#     crypt_pwd = user_info[""]
#     is_auth = verify_user(pwd=e_pwd, crypt_pwd=crypt_pwd)

#     url = request.url_for("dashboard")
#     return RedirectResponse(url, status_code=303)


# async def logout(request):
#     request.session.clear()
#     url = request.url_for("dashboard")
#     return RedirectResponse(url, status_code=303)


# async def verify_user(encoded_pwd: str, crypt_pwd: str) -> bool:
#     logger.info(f"verifing password")
#     pwd = base64.decode(encoded_pwd)
#     result = await verify_pass(pwd=pwd, crypt_pwd=crypt_pwd)
#     return result
from starlette.responses import RedirectResponse
from starlette.datastructures import URL

# from source import settings, tables
from app_functions.db_setup import database, users

import settings

# from source.resources import database
import datetime


async def login(request):
    from main import GITHUB_AUTH_URL

    query = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "redirect_url": request.url_for("auth:callback"),
    }
    url = URL(GITHUB_AUTH_URL).include_query_params(**query)
    return RedirectResponse(url, status_code=303)


async def logout(request):
    request.session.clear()
    url = request.url_for("dashboard")
    return RedirectResponse(url, status_code=303)


async def callback(request):
    from main import github_client, github_api_client

    # Obtain an access token.
    code = request.query_params.get("code", "")
    url = "/login/oauth/access_token"
    data = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code,
    }
    headers = {"accept": "application/json"}
    response = await github_client.post(url, data=data, headers=headers)
    response.raise_for_status()
    data = response.json()
    #  Make a request to the API.
    url = "/user"
    headers = {
        "authorization": f'token {data["access_token"]}',
    }
    response = await github_api_client.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Log the user in, and redirect back to the homepage.
    query = users.select().where(users.c.github_id == data["id"])
    user = await database.fetch_one(query)
    if user is None:

        query = users.insert()
        values = {
            "created_at": datetime.datetime.now(),
            "last_login": datetime.datetime.now(),
            "username": data["login"],
            "github_id": data["id"],
            "is_admin": False,
            "name": data["name"],
            "avatar_url": data["avatar_url"],
        }
    else:
        query = users.update().where(users.c.github_id == data["id"])
        values = {
            "last_login": datetime.datetime.now(),
            "username": data["login"],
            "name": data["name"],
            "avatar_url": data["avatar_url"],
        }
    await database.execute(query, values=values)

    request.session["username"] = data["login"]
    request.session["avatar_url"] = data["avatar_url"]
    url = request.url_for("profile", username=data["login"])
    # url="/mydata"
    return RedirectResponse(url, status_code=303)
