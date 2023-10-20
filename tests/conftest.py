import os

import pytest

from tests.test_data.sender_id import (
    fetch_payload as fetch_sender_id_payload,
    request_payload as request_sender_id_payload,
)
from tests.test_data.messaging import data as messaging_response
from tests.test_data.campaign import (
    get_phonebook,
    get_contacts,
    add_contact,
    fetch_campaigns,
    fetch_campaign_history,
)
from termii.utils import requests
from tests.test_data.token import (
    send_token_response,
    voice_token_response,
    email_token_response,
    verify_token,
    in_app_token_response,
)


@pytest.fixture()
def test_environments():
    """
    Add required variables to environment.
    """
    os.environ["TERMII_API_KEY"] = "ukwiwe4642eh"
    os.environ["TERMII_ENDPOINT_URL"] = "https://api.ng.termii.com"
    os.environ["TERMII_SENDER_ID"] = "Test"


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


class MockGetContactsResponse:
    status_code = 200

    @staticmethod
    def json():
        return get_contacts


@pytest.fixture()
def mock_get_contacts(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockGetContactsResponse()

    monkeypatch.setattr(requests, "get", mock_get)


class MockAddContactsResponse:
    status_code = 200

    @staticmethod
    def json():
        return add_contact


@pytest.fixture()
def mock_add_contacts(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockAddContactsResponse()

    monkeypatch.setattr(requests, "post", mock_post)


class MockAddMultipleContactsResponse:
    status_code = 200

    @staticmethod
    def json():
        return {"message": "Your list is being uploaded in the background."}


@pytest.fixture()
def mock_add_multi_contacts(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockAddMultipleContactsResponse()

    monkeypatch.setattr(requests, "post", mock_post)


class MockDeleteContactResponse:
    status_code = 200

    @staticmethod
    def json():
        return {"message": "Contact deleted successfully"}


@pytest.fixture()
def mock_delete_contact(monkeypatch):
    def mock_delete(*args, **kwargs):
        return MockDeleteContactResponse()

    monkeypatch.setattr(requests, "delete", mock_delete)


class MockSendCampaignResponse:
    status_code = 200

    @staticmethod
    def json():
        return {"message": "Your campaign has been scheduled"}


@pytest.fixture()
def mock_send_campaign_contact(monkeypatch):
    def mock_send_campaign(*args, **kwargs):
        return MockSendCampaignResponse()

    monkeypatch.setattr(requests, "post", mock_send_campaign)


class MockFetchCampaignsResponse:
    status_code = 200

    @staticmethod
    def json():
        return fetch_campaigns


@pytest.fixture()
def mock_fetch_campaigns(monkeypatch):
    def mock_fetch_campaign(*args, **kwargs):
        return MockFetchCampaignsResponse()

    monkeypatch.setattr(requests, "get", mock_fetch_campaign)


class MockFetchCampaignHistoryResponse:
    status_code = 200

    @staticmethod
    def json():
        return fetch_campaign_history


@pytest.fixture()
def mock_fetch_campaign_history(monkeypatch):
    def mock_fetch_campaign(*args, **kwargs):
        return MockFetchCampaignHistoryResponse()

    monkeypatch.setattr(requests, "get", mock_fetch_campaign)


class MockSendTokenResponse:
    status_code = 200

    @staticmethod
    def json():
        return send_token_response


@pytest.fixture()
def mock_send_token_response(monkeypatch):
    def mock_send_token(*args, **kwargs):
        return MockSendTokenResponse()

    monkeypatch.setattr(requests, "post", mock_send_token)


class MockSendVoiceTokenResponse:
    status_code = 200

    @staticmethod
    def json():
        return voice_token_response


@pytest.fixture()
def mock_send_voice_token_response(monkeypatch):
    def mock_voice_send_token(*args, **kwargs):
        return MockSendVoiceTokenResponse()

    monkeypatch.setattr(requests, "post", mock_voice_send_token)


class MockEmailTokenResponse:
    status_code = 200

    @staticmethod
    def json():
        return email_token_response


@pytest.fixture()
def mock_email_token_response(monkeypatch):
    def mock_email_token(*args, **kwargs):
        return MockEmailTokenResponse()

    monkeypatch.setattr(requests, "post", mock_email_token)


class MockVerifyTokenResponse:
    status_code = 200

    @staticmethod
    def json():
        return verify_token


@pytest.fixture()
def mock_verify_token_response(monkeypatch):
    def mock_verify_token(*args, **kwargs):
        return MockVerifyTokenResponse()

    monkeypatch.setattr(requests, "post", mock_verify_token)


class MockInAppTokenResponse:
    status_code = 200

    @staticmethod
    def json():
        return in_app_token_response


@pytest.fixture()
def mock_in_app_token_response(monkeypatch):
    def mock_token(*args, **kwargs):
        return MockInAppTokenResponse()

    monkeypatch.setattr(requests, "post", mock_token)
