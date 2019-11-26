# -*- coding: utf-8 -*-
from starlette.routing import Mount, Route, Router

# from .pages import page_routes
from .main import views as main_views
from .pages import views as page_views

# from .main import app as home_routes


# mounted app can also be an instance of `Router()`
# Mount("/", app=home_routes),
# Mount("/pages/", app=public_routes),
routes = Router(
    [
        Route("/", main_views.homepage, methods=["GET", "POST"]),
        Route("/{page}", main_views.homepage_page, methods=["GET", "POST"]),
        Mount(
            "/pages",
            app=Router(
                [
                    Route(
                        "/{page}",
                        endpoint=page_views.example_pages,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/error/{page}",
                        endpoint=page_views.example_pages,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/charts/{page}",
                        endpoint=page_views.example_pages_charts,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/forms/{page}",
                        endpoint=page_views.example_pages_forms,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/examples/{page}",
                        endpoint=page_views.example_pages_examples,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/mailbox/{page}",
                        endpoint=page_views.example_pages_mailbox,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/tables/{page}",
                        endpoint=page_views.example_pages_tables,
                        methods=["GET", "POST"],
                    ),
                    Route(
                        "/ui/{page}",
                        endpoint=page_views.example_pages_ui,
                        methods=["GET", "POST"],
                    ),
                ]
            ),
        ),
        # Mount(
        #     "/pages/charts",
        #     app=Router(
        #         [
        #             Route(
        #                 "/{page}",
        #                 endpoint=page_views.example_pages_charts,
        #                 methods=["GET", "POST"],
        #             ),
        #         ]
        #     ),
        # ),
    ]
)
