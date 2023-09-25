from typing import Dict, Optional

from termii.auth import Client

from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.campaign import (
    FETCH_PHONEBOOKS,
    CREATE_PHONEBOOK,
    UPDATE_PHONEBOOK,
    DELETE_PHONEBOOK,
)


class Campaign(Client):
    """
    Handle operations related to phonebook.
    """

    def get_phonebooks(self, page: Optional[int] = 1) -> Dict:
        """
        Get all saved phonebooks.

        Args:
            `page` (int): Page to return. Starts at 1.
        """

        self.validate_authentication()
        data = RequestData(
            url=FETCH_PHONEBOOKS.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                page=page,
            ),
            type=RequestType.get,
        )
        return make_request(data=data)

    def create_phonebook(self, name: str, description: str) -> Dict:
        """
        Create a phonebook.

        Args:
            `name` (str): The name of the phonebook.

            `description` (str): A description of the contacts stored in the phonebook.
        """  # noqa
        self.validate_authentication()
        payload = dict(
            api_key=self.TERMII_API_KEY,
            phonebook_name=name,
            description=description,
        )
        request_data = RequestData(
            url=CREATE_PHONEBOOK.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def update_phonebook(
        self, name: str, description: str, phonebook_id: str
    ) -> Dict:
        """
        Update a phonebook.

        Args:
            `name` (str): The name of the phonebook.

            `description` (str): A description of the contacts stored in the phonebook.

            `phonebook_id` (str): ID of phonebook to update.
        """  # noqa
        self.validate_authentication()
        payload = dict(
            api_key=self.TERMII_API_KEY,
            phonebook_name=name,
            description=description,
        )
        request_data = RequestData(
            url=UPDATE_PHONEBOOK.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                phonebook_id=phonebook_id,
            ),
            payload=payload,
            type=RequestType.patch,
        )
        return make_request(data=request_data)

    def delete_phonebook(self, phonebook_id: str) -> Dict:
        """
        Delete a phonebook.

        Args:

            `phonebook_id` (str): ID of phonebook to update.
        """
        self.validate_authentication()
        request_data = RequestData(
            url=DELETE_PHONEBOOK.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                phonebook_id=phonebook_id,
                TERMII_API_KEY=self.TERMII_API_KEY,
            ),
            type=RequestType.delete,
        )
        return make_request(data=request_data)
