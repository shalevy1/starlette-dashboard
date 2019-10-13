import requests
from loguru import logger

from com_lib.file_functions import open_json


def call_api():
    """ call test-api to fetch fake users.  """
    # TODO: Consider changing to encode/httpx when stable https://github.com/encode/httpx

    try:
        # test-api is built with FastAPI (https://fastapi.tiangolo.com), which is built on top of Starlette
        r = requests.get(
            "https://test-api.devsetgo.com/api/v1/users/list?qty=500", timeout=2
        )
        logger.info(f"API Call Status Code: {r.status_code} from test-api.devsetgo.com")
        resp = r.json()
        obj = resp["users"]
        logger.info(f"serving test-api response")
        return obj
    except Exception as e:
        logger.error(f"error: API was non-responsive: {e}")
        obj = open_json("people_sample.json")
        logger.info(f"serving sample.json due to API non-response")
        return obj
