import pytest

from termii.token import Token
from termii.utils import get_random_numbers
from termii.schemas.token import TokenType
from tests.test_data.token import send_token_response


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
