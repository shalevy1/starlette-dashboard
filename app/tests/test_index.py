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
    def test_index(self):
        url = f"/"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 200

    def test_index_pages(self):
        pages = ['index','index2','index3']
        
        for page in pages:
            url = f"/{page}"
            client = TestClient(app)
            response = client.get(url)
            assert response.status_code == 200


    def test_index__error(self):
        uid = uuid.uuid1()
        url = f"/{uid}"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 404
