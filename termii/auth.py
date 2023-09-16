import os


class Client:
    def authenticate_from_env(self) -> None:
        """
        Authenticate requests using variables in the environment.
        Method expects the following variables to be present in the environment:
            `TERMII_API_KEY`, `TERMII_ENDPOINT_URL`, `TERMII_SENDER_ID`

        Raises:
            `ValueError`: If any of the expected environment variables are not present.
        """  # noqa

        # Get variables.
        environment = os.environ
        self.TERMII_API_KEY = environment.get("TERMII_API_KEY")
        self.TERMII_ENDPOINT_URL = environment.get("TERMII_ENDPOINT_URL")
        self.TERMII_SENDER_ID = environment.get("TERMII_SENDER_ID")

        # Validate variables.
        if self.TERMII_API_KEY is None:
            raise ValueError(
                "TERMII_API_KEY is not present in the environment."
            )
        if self.TERMII_ENDPOINT_URL is None:
            raise ValueError(
                "TERMII_ENDPOINT_URL is not present in the environment."
            )
        if self.TERMII_SENDER_ID is None:
            raise ValueError(
                "TERMII_SENDER_ID is not present in the environment."
            )

    def authenticate_direct(
        self, api_key: str, endpoint_url: str, sender_id: str
    ) -> None:
        """
        Directly authenticate with entered values.

        Args:
            `api_key` (str): API key from Termii dashboard.

            `endpoint_url` (str): Endpoint url from Termii dashboard.

            `sender_id` (str): Sender ID from Termii dashboard.
        """
        self.TERMII_API_KEY = api_key
        self.TERMII_ENDPOINT_URL = endpoint_url
        self.TERMII_SENDER_ID = sender_id
