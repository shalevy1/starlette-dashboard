# -*- coding: utf-8 -*-
import datetime
import os
import sys
import time
import unittest
import uuid
from unittest import mock

import pytest
import requests
import requests_mock
from requests.exceptions import Timeout
from starlette.exceptions import HTTPException
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

from app.main import app, debug_mode
from routes.pages.functions import call_api

client = TestClient(app)


class Test(unittest.TestCase):
    def test_call_api(self):
        # with pytest.raises(Exception):
        result = call_api()
        assert len(result) != 0

    # def test_call_api_error(self):

    #     with pytest.raises(Exception):
    #         assert call_api()
