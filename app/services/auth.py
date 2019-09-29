# -*- coding: utf-8 -*-
import base64
import binascii

from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    AuthenticationMiddleware,
    SimpleUser,
    UnauthenticatedUser,
    requires,
)
from starlette.responses import PlainTextResponse


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decoded.partition(":")
        # TODO: You'd want to verify the username and password here,
        #       possibly by installing `DatabaseMiddleware`
        #       and retrieving user information from `request.database`.
        return AuthCredentials(["authenticated"]), SimpleUser(username)


app = Starlette()
app.add_middleware(AuthenticationMiddleware, backend=BasicAuthBackend())


@app.route("/")
@requires(["authenticated", "admin"], status_code=404)
async def homepage(request):
    if request.user.is_authenticated:
        return PlainTextResponse("hello, " + request.user.display_name)
    return PlainTextResponse("hello, you")
