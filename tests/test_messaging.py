import os

import pytest
from termii.messaging.core import Messaging

from tests.test_data.sender_id import fetch_payload as fetch_sender_id_payload


class TestSenderID:
    def test_fetch_sender_id(self, test_environments, mock_fetch_sender_id):
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()
        sender_ids = messaging_client.fetch_sender_id(page=1)
        assert sender_ids is not None

        print(sender_ids)
        assert len(sender_ids["data"]) == len(fetch_sender_id_payload["data"])

    def test_fetch_sender_id_without_auth(
        self, test_environments, mock_fetch_sender_id
    ):
        del os.environ["TERMII_API_KEY"]
        del os.environ["TERMII_ENDPOINT_URL"]
        del os.environ["TERMII_SENDER_ID"]

        messaging_client = Messaging()
        with pytest.raises(ValueError) as value_error:
            messaging_client.fetch_sender_id(page=1)

        assert str(value_error.value) == "Authentication required."

    def test_request_sender_id(self, mock_request_sender_id):
        messaging_client = Messaging()
        result = messaging_client.request_sender_id(
            sender_id="test id",
            usecase="test use case",
            company="test company",
            api_key="Test key",
            endpoint_url="https://api.ng.termii.com",
        )
        assert result is not None
        assert result.get("code") == "ok"
        assert (
            result.get("message")
            == "Sender Id requested. You will be  contacted by your account manager."  # noqa
        )
