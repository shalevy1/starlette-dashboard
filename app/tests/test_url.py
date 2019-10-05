# -*- coding: utf-8 -*-
import datetime
import os
import sys
import time
import uuid
import unittest
from unittest import mock
import requests
from requests.exceptions import Timeout
import requests_mock

import pytest
from app.main import app, debug_mode, call_api
from starlette.responses import HTMLResponse
from starlette.testclient import TestClient
from starlette.exceptions import HTTPException

client = TestClient(app)


class Test(unittest.TestCase):
    def test_index(self):
        client = TestClient(app)
        response = client.get("/")
        assert response.status_code == 200

    def test_cards(self):
        client = TestClient(app)
        response = client.get("/example/form")
        assert response.status_code == 200

    def test_login(self):
        client = TestClient(app)
        response = client.get("/example/login")
        assert response.status_code == 200

    def test_404(self):
        uid = uuid.uuid1()
        uid_str = str(uid)
        url = f"/whale-{uid_str}"

        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 404

    # TODO: determine why exceptions are not being tested properly
    def test_index_error(self):
        client = TestClient(app)
        m = mock.Mock()
        m.side_effect = Exception(client.get("/"))
        try:
            m()
        except Exception:
            assert True

    # TODO: determine why exceptions are not being tested properly
    def test_cards_error(self):
        client = TestClient(app, raise_server_exceptions=False)
        m = mock.Mock()
        m.side_effect = Exception(client.get("/example/cards"))
        try:
            m()
        except Exception:
            assert True

    def test_call_api(self):
        # with pytest.raises(Exception):
        result = call_api()
        assert len(result) != 0

    # TODO: determine why exceptions are not being tested properly
    def test_call_api_error(self):
        m = mock.Mock()
        m.side_effect = Exception(call_api())
        try:
            m()
        except Exception:
            assert True


# TODO: determine why exceptions are not being tested properly
