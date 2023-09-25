import os

import pytest

from tests.test_data.sender_id import (
    fetch_payload as fetch_sender_id_payload,
    request_payload as request_sender_id_payload,
)
from tests.test_data.messaging import data as messaging_response
from tests.test_data.campaign import get_phonebook
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


class MockMessageResponse:
    status_code = 200

    @staticmethod
    def json():
        return messaging_response


@pytest.fixture()
def mock_send_messaging(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockMessageResponse()

    monkeypatch.setattr(requests, "post", mock_post)


class MockGetPhonebookResponse:
    status_code = 200

    @staticmethod
    def json():
        return get_phonebook


@pytest.fixture()
def mock_get_phonebook(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockGetPhonebookResponse()

    monkeypatch.setattr(requests, "get", mock_get)


class MockCreatePhonebookResponse:
    status_code = 200

    @staticmethod
    def json():
        return {"message": "Phonebook added successfully"}


@pytest.fixture()
def mock_create_phonebook(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockCreatePhonebookResponse()

    monkeypatch.setattr(requests, "post", mock_post)


class MockUpdatePhonebookResponse:
    status_code = 200

    @staticmethod
    def json():
        return {"message": "Phonebook updated successfully"}


@pytest.fixture()
def mock_update_phonebook(monkeypatch):
    def mock_patch(*args, **kwargs):
        return MockUpdatePhonebookResponse()

    monkeypatch.setattr(requests, "patch", mock_patch)


class MockDeletePhonebookResponse:
    status_code = 200

    @staticmethod
    def json():
        return {"message": "Phonebook deleted successfully"}


@pytest.fixture()
def mock_delete_phonebook(monkeypatch):
    def mock_delete(*args, **kwargs):
        return MockDeletePhonebookResponse()

    monkeypatch.setattr(requests, "delete", mock_delete)
