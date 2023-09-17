import os

import pytest
from termii.auth import Client


class TestClient:
    def test_authenticate_behaviour_if_no_api_key(self, test_environments):
        """
        Test authentication behaviour if no TERMII_API_KEY is added
        to the environment.
        """
        del os.environ["TERMII_API_KEY"]

        termii_client = Client()
        with pytest.raises(ValueError) as value_error:
            termii_client.authenticate_from_env()
            assert (
                str(value_error.value)
                == "TERMII_API_KEY is not present in the environment."
            )

    def test_authenticate_behaviour_if_no_endpoint_url(
        self, test_environments
    ):
        """
        Test authentication behaviour if no TERMII_ENDPOINT_URL
        is added to the environment.
        """
        del os.environ["TERMII_ENDPOINT_URL"]

        termii_client = Client()
        with pytest.raises(ValueError) as value_error:
            termii_client.authenticate_from_env()
        assert (
            str(value_error.value)
            == "TERMII_ENDPOINT_URL is not present in the environment."
        )

    def test_authenticate_behaviour_if_no_sender_id(self, test_environments):
        """
        Test authentication behaviour if no TERMII_SENDER_ID is
        added to the environment.
        """
        del os.environ["TERMII_SENDER_ID"]

        termii_client = Client()
        with pytest.raises(ValueError) as value_error:
            termii_client.authenticate_from_env()
        assert (
            str(value_error.value)
            == "TERMII_SENDER_ID is not present in the environment."
        )

    def test_authenticate_client_by_env(self, test_environments):
        """Test that env authentication works."""
        termii_client = Client()
        termii_client.authenticate_from_env()
        assert termii_client.TERMII_API_KEY == os.environ["TERMII_API_KEY"]
        assert (
            termii_client.TERMII_ENDPOINT_URL
            == os.environ["TERMII_ENDPOINT_URL"]
        )
        assert termii_client.TERMII_SENDER_ID == os.environ["TERMII_SENDER_ID"]

    def test_authenticate_direct(self, test_environments):
        """Test that direct authentication."""

        api_key = "test_key"
        endpoint_url = "https://api.ng.termii.com"
        sender_id = "test_id"

        termii_client = Client()
        termii_client.authenticate_direct(
            api_key=api_key, endpoint_url=endpoint_url, sender_id=sender_id
        )

        assert termii_client.TERMII_API_KEY == api_key
        assert termii_client.TERMII_ENDPOINT_URL == endpoint_url
        assert termii_client.TERMII_SENDER_ID == sender_id
