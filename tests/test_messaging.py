import os

import pytest

from termii.messaging import Messaging
from tests.test_data.sender_id import fetch_payload as fetch_sender_id_payload
from termii.schemas.messaging import (
    MessagingChannel,
    MessageDistributionType,
)
from termii.utils import get_random_numbers


class TestSenderID:
    def test_fetch_sender_id(self, test_environments, mock_fetch_sender_id):
        """Test fetch of sender id"""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()
        sender_ids = messaging_client.fetch_sender_id(page=1)
        assert sender_ids is not None

        print(sender_ids)
        assert len(sender_ids["data"]) == len(fetch_sender_id_payload["data"])

    def test_fetch_sender_id_without_auth(
        self, test_environments, mock_fetch_sender_id
    ):
        """Test fetch of sender ID without authentication"""
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


class TestSendSimpleMessage:
    def test_send_1(self, test_environments, mock_send_messaging):
        """Test send of simple messages."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(50)]
        response = messaging_client.send_message(
            receivers=receivers, text="Hello all. Thanks for visiting."
        )
        assert response["message"] == "Successfully Sent"

    def test_send_max_receipients(
        self, test_environments, mock_send_messaging
    ):
        """Test send of simple messages if recepients are beyond max limit."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(500)]
        with pytest.raises(ValueError) as value_error:
            messaging_client.send_message(
                receivers=receivers, text="Hello all. Thanks for visiting."
            )
        assert (
            str(value_error.value)
            == "You cannot send to more than 100 mobile numbers."
        )

    def test_send_bulk_max_receipients(
        self, test_environments, mock_send_messaging
    ):
        """Test send of bulk messages if recepients are beyond max limit."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(20000)]
        with pytest.raises(ValueError) as value_error:
            messaging_client.send_message(
                receivers=receivers,
                text="Hello all. Thanks for visiting.",
                distribution_type=MessageDistributionType.bulk,
            )
        assert (
            str(value_error.value)
            == "You cannot send to more than 10000 mobile numbers."
        )

    def test_send_simple_message_with_media(
        self, test_environments, mock_send_messaging
    ):
        """Test behaviour if simple message has a media."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(20000)]
        with pytest.raises(ValueError) as value_error:
            messaging_client.send_message(
                receivers=receivers,
                text="Hello all. Thanks for visiting.",
                distribution_type=MessageDistributionType.bulk,
                media_url="http://test.com/hello.jpeg",
            )
        assert (
            str(value_error.value)
            == "Media messages are only allowed with whatsapp channel."
        )

    def test_send_bulk(self, test_environments, mock_send_messaging):
        """Test send of bulk messages."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(50)]
        response = messaging_client.send_message(
            receivers=receivers,
            text="Hello all. Thanks for visiting.",
            distribution_type=MessageDistributionType.bulk,
        )
        assert response["message"] == "Successfully Sent"

    def test_send_whatsapp_bulk(self, test_environments, mock_send_messaging):
        """Test send of bulk whatsapp messages."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(50)]
        response = messaging_client.send_message(
            receivers=receivers,
            text="Hello all. Thanks for visiting.",
            distribution_type=MessageDistributionType.bulk,
            channel=MessagingChannel.whatsapp,
        )
        assert response["message"] == "Successfully Sent"

    def test_send_from_autogenerated_number(
        self, test_environments, mock_send_messaging
    ):
        """Test send message from autogenerated number."""
        messaging_client = Messaging()
        messaging_client.authenticate_from_env()

        receivers = [get_random_numbers(13) for _ in range(50)]
        response = messaging_client.send_message_from_autogenerated_number(
            receivers=receivers,
            text="Hello all. Thanks for visiting.",
        )
        assert response["message"] == "Successfully Sent"
