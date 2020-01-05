# -*- coding: utf-8 -*-
# from starlette.routing import Route, Mount
# from starlette.staticfiles import StaticFiles
# from endpoints.pages import endpoints


# routes = [
#     Route("/{page}", endpoint=endpoints.example_pages, methods=["GET"]),
#     Route("/charts/{page}", endpoint=endpoints.example_pages_charts, methods=["GET"]),
#     Route(
#         "/examples/{page}", endpoint=endpoints.example_pages_examples, methods=["GET"]
#     ),
#     Route("/forms/{page}", endpoint=endpoints.example_pages_forms, methods=["GET"]),
#     Route("/mailbox/{page}", endpoint=endpoints.example_pages_mailbox, methods=["GET"]),
#     Route(
#         "/data_tables/{page}", endpoint=endpoints.example_pages_tables, methods=["GET"]
#     ),
#     Route("/ui/{page}", endpoint=endpoints.example_pages_ui, methods=["GET"]),
#     Mount("/static", app=StaticFiles(directory="statics"), name="static"),
# ]
