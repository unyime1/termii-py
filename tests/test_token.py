import uuid

import pytest

from termii.token import Token
from termii.utils import get_random_numbers, get_random_string
from termii.schemas.token import TokenType
from tests.test_data.token import (
    send_token_response,
    voice_token_response,
    email_token_response,
    verify_token,
    in_app_token_response,
)


class TestSendToken:
    def test_send_token(self, test_environments, mock_send_token_response):
        """Test send token"""
        token_client = Token()
        token_client.authenticate_from_env()
        response = token_client.send_token(
            message_type=TokenType.ALPHANUMERIC,
            receiver=get_random_numbers(count=10),
        )
        assert response.get("pinId") == send_token_response.get("pinId")

    def test_send_token_pin_attempts(
        self, test_environments, mock_send_token_response
    ):
        """Test send token with higher pin limit"""
        token_client = Token()
        token_client.authenticate_from_env()

        with pytest.raises(ValueError) as value_error:
            token_client.send_token(
                message_type=TokenType.ALPHANUMERIC,
                receiver=get_random_numbers(count=10),
                pin_attempts=0,
            )
        assert str(value_error.value) == "Pin attempts must be atleast 1."

    def test_send_token_pin_time_to_live(
        self, test_environments, mock_send_token_response
    ):
        """Test send token with pin_time_to_live limit"""
        token_client = Token()
        token_client.authenticate_from_env()

        with pytest.raises(ValueError) as value_error:
            token_client.send_token(
                message_type=TokenType.ALPHANUMERIC,
                receiver=get_random_numbers(count=10),
                pin_time_to_live=70,
            )
        assert (
            str(value_error.value)
            == "pin_time_to_live must be between 0 and 60."
        )

    def test_send_token_validate_pin_length(
        self, test_environments, mock_send_token_response
    ):
        """Test send token with pin_time_to_live limit"""
        token_client = Token()
        token_client.authenticate_from_env()

        with pytest.raises(ValueError) as value_error:
            token_client.send_token(
                message_type=TokenType.ALPHANUMERIC,
                receiver=get_random_numbers(count=10),
                pin_length=40,
            )
        assert str(value_error.value) == "pin_length must be between 4 and 8."

    def test_send_token_validate_message_text(
        self, test_environments, mock_send_token_response
    ):
        """Test send token with pin_time_to_live limit"""
        token_client = Token()
        token_client.authenticate_from_env()

        with pytest.raises(ValueError) as value_error:
            token_client.send_token(
                message_type=TokenType.ALPHANUMERIC,
                receiver=get_random_numbers(count=10),
                pin_placeholder="uryue",
            )
        assert (
            str(value_error.value)
            == "Your pin_placeholder must be in message_text."
        )


class TestSendVoiceToken:
    def test_send_voice_token(
        self, test_environments, mock_send_voice_token_response
    ):
        """Test send token"""
        token_client = Token()
        token_client.authenticate_from_env()
        response = token_client.send_voice_token(
            phone_number=get_random_numbers(count=10),
        )
        assert response.get("pinId") == voice_token_response.get("pinId")


class TestVoiceCall:
    def test_voice_call(
        self, test_environments, mock_send_voice_token_response
    ):
        """Test voice call"""
        token_client = Token()
        token_client.authenticate_from_env()
        response = token_client.voice_call(
            phone_number=get_random_numbers(count=10), code=6534
        )
        assert response.get("pinId") == voice_token_response.get("pinId")

    def test_voice_call_non_numerical(
        self, test_environments, mock_send_voice_token_response
    ):
        """Test voice call"""
        token_client = Token()
        token_client.authenticate_from_env()
        with pytest.raises(ValueError) as value_error:
            token_client.voice_call(
                phone_number=get_random_numbers(count=10),
                code=get_random_string(4),
            )
        assert str(value_error.value) == "Code must be numerical."


class TestEmailToken:
    def test_email_token(self, test_environments, mock_email_token_response):
        """Test voice call"""
        token_client = Token()
        token_client.authenticate_from_env()
        response = token_client.email_token(
            email_address="test@termii.com",
            code=get_random_string(4),
            email_configuration_id=get_random_string(26),
        )
        assert response.get("message_id") == email_token_response.get(
            "message_id"
        )


class TestVerifyToken:
    def test_verify_token(self, test_environments, mock_verify_token_response):
        """Test voice call"""
        token_client = Token()
        token_client.authenticate_from_env()
        response = token_client.verify_token(
            pin_id=str(uuid.uuid4()), pin=get_random_numbers(6)
        )
        assert response.get("pinId") == verify_token.get("pinId")


class TestGetInAppToken:
    def test_get_in_app_token(
        self, test_environments, mock_in_app_token_response
    ):
        """Test send token"""
        token_client = Token()
        token_client.authenticate_from_env()
        response = token_client.in_app_token(
            pin_type=TokenType.ALPHANUMERIC,
            phone_number=get_random_numbers(count=10),
        )
        assert response.get("status") == in_app_token_response.get("status")
