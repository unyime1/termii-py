from typing import Dict, Optional

from termii.auth import Client
from termii.messaging.schemas import RequestData, RequestType
from termii.messaging.endpoints import FETCH_SENDER_ID, REQUEST_SENDER_ID
from termii.utils import make_request


class Messaging(Client):
    """
    Base class for core messaging APIs.
    """

    def validate_authentication(self) -> None:
        """
        Ensure that API keys are provided.
        """
        if (
            not hasattr(self, "TERMII_API_KEY")
            or not hasattr(self, "TERMII_ENDPOINT_URL")
            or not hasattr(self, "TERMII_SENDER_ID")
        ):
            raise ValueError("Authentication required.")

    def fetch_sender_id(self, page: Optional[int] = 1) -> Dict:
        """
        `Documentation`: https://developers.termii.com/sender-id

        Fetch sender IDs from API.

        Args:
            `page` (int, None): Page to fetch. Starts from 1.

        Returns:
            Dict.
        """
        self.validate_authentication()

        # Prepare request.
        data = RequestData(
            url=FETCH_SENDER_ID.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                data_page=page,
            ),
            type=RequestType.get,
        )
        return make_request(data=data)

    def request_sender_id(
        self,
        sender_id: str,
        usecase: str,
        company: str,
        api_key: str,
        endpoint_url: str,
    ) -> Dict:
        """
        `Documentation`: https://developers.termii.com/sender-id

        Request new sender ID from API.

        Args:
            `sender_id` (str): Represents the ID of the sender which can be
            alphanumeric or numeric. Alphanumeric sender ID length
            should be between 3 and 11 characters (Example:CompanyName)

            `usecase` (str): A sample of the type of message sent.

            `company` (str): Represents the name of the company with the
                            sender ID.

            `api_key` (str): API key from Termii dashboard.

            `endpoint_url` (str): Endpoint url from dashboard.
            E.g https://api.ng.termii.com
        Returns:
            Dict.
        """
        payload = dict(
            api_key=api_key,
            sender_id=sender_id,
            usecase=usecase,
            company=company,
        )
        request_data = RequestData(
            url=REQUEST_SENDER_ID.format(TERMII_ENDPOINT_URL=endpoint_url),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)
