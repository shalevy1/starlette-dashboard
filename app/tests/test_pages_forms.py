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
    def test_pages_forms(self):
        pages = ["advanced", "editors", "general", "validation"]

        for page in pages:
            url = f"/pages/forms/{page}"
            client = TestClient(app)
            response = client.get(url)
            assert response.status_code == 200

    def test_pages_forms_error(self):
        uid = uuid.uuid1()
        url = f"/pages/forms/{uid}"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 404
