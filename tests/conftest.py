import os

import pytest

from tests.test_data.sender_id import (
    fetch_payload as fetch_sender_id_payload,
    request_payload as request_sender_id_payload,
)
from termii.utils import requests


@pytest.fixture()
def test_environments():
    """
    Add required variables to environment.
    """
    os.environ["TERMII_API_KEY"] = "test123"
    os.environ["TERMII_ENDPOINT_URL"] = "https://api.ng.termii.com"
    os.environ["TERMII_SENDER_ID"] = "test"


class MockFetchSenderIDResponse:
    status_code = 200

    @staticmethod
    def json():
        return fetch_sender_id_payload


@pytest.fixture()
def mock_fetch_sender_id(monkeypatch):
    """Requests.get() mocked to return custom response."""

    def mock_get(*args, **kwargs):
        return MockFetchSenderIDResponse()

    monkeypatch.setattr(requests, "get", mock_get)


class MockRequestSenderIDResponse:
    status_code = 200

    @staticmethod
    def json():
        return request_sender_id_payload


@pytest.fixture()
def mock_request_sender_id(monkeypatch):
    """Requests.get() mocked to return custom response."""

    def mock_post(*args, **kwargs):
        return MockRequestSenderIDResponse()

    monkeypatch.setattr(requests, "post", mock_post)
