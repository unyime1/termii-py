import os

import pytest


@pytest.fixture()
def test_environments():
    """
    Add required variables to environment.
    """
    os.environ["TERMII_API_KEY"] = "test123"
    os.environ["TERMII_ENDPOINT_URL"] = "https://api.ng.termii.com"
    os.environ["TERMII_SENDER_ID"] = "test"
