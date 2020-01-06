# -*- coding: utf-8 -*-
from loguru import logger
from starlette.exceptions import HTTPException
from resources import templates
from app_functions.db_setup import users, database
from endpoints.main.github_calls import get_repo_list


async def homepage(request):

    # return responses.PlainTextResponse("Hello, main")
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


# async def my_data(request):
#     username = request.path_params["username"]
#     # can_edit = check_can_edit(request, username)

#     query = users.select().where(users.c.username == username)
#     profile_user = await database.fetch_one(query)
#     if profile_user is None:
#         raise HTTPException(status_code=404)

#     status_code = 200

#     template = "profile.html"
#     context = {
#         "request": request,
#         "owner": username,
#         "profile_user": profile_user,
#         # "rows": rows,
#         # "form_values": form_values,
#         # "form_errors": form_errors,
#         # "can_edit": can_edit,
#     }
#     return templates.TemplateResponse(template, context, status_code=status_code)


async def profile(request):

    if "username" not in request.session:
        logger.error(
            f"user page access without being logged in from {request.client.host}"
        )
        raise HTTPException(status_code=403)

    username = request.path_params["username"]
    # can_edit = check_can_edit(request, username)

    query = users.select().where(users.c.username == username)
    profile_user = await database.fetch_one(query)
    if profile_user is None:
        raise HTTPException(status_code=403)

    repo_data = await get_repo_list("devsetgo")

    # datasources = await load_datasources_for_user(profile_user)

    # rows = []
    # for datasource in datasources:
    #     text = datasource.name
    #     url = datasource.url
    #     count = await datasource.count()
    #     rows.append({"text": text, "url": url, "count": count})

    # if request.method == "POST":
    #     form_values = await request.form()
    #     validated_data, form_errors = NewTableSchema.validate_or_error(form_values)
    #     if not form_errors:
    #         identity = slugify(validated_data["name"], to_lower=True)
    #         query = (
    #             tables.table.select()
    #             .where(tables.table.c.user_id == profile_user["pk"])
    #             .where(tables.table.c.identity == identity)
    #         )
    #         table = await database.fetch_one(query)
    #         if table is not None:
    #             form_errors = {"name": "A table with this name already exists."}

    #     if not form_errors:
    #         insert_data = dict(validated_data)
    #         insert_data["created_at"] = datetime.datetime.now()
    #         insert_data["identity"] = slugify(insert_data["name"], to_lower=True)
    #         insert_data["user_id"] = profile_user["pk"]
    #         query = tables.table.insert()
    #         await database.execute(query, values=insert_data)
    #         return RedirectResponse(url=request.url, status_code=303)
    #     status_code = 400
    # else:
    #     form_values = None
    #     form_errors = None
    status_code = 200
    template = "profile.html"
    context = {
        "request": request,
        "owner": username,
        "profile_user": profile_user,
        "repo_data": repo_data,
        # "rows": rows,
        # "form_values": form_values,
        # "form_errors": form_errors,
        # "can_edit": can_edit,
    }
    return templates.TemplateResponse(template, context, status_code=status_code)
    # except Exception as e:
    #     detail="user is not logged in"
    #     logger.critical(
    #         f"Error: The user is not logged in. {e}"
    #     )
    #     raise HTTPException(403, detail=detail)


async def profile_repo():

    return "x"
