from typing import Dict, Optional

from termii.auth import Client

from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.contacts import (
    FETCH_CONTACTS
)


class Contacts(Client):
    def get_contacts(self, phonebook_id: str, page: Optional[int] = 1) -> Dict:
        """
        Get all contacts on phonebook.
        Docs: https://developers.termii.com/contacts

        Args:
            `page` (int): Page to return. Starts at 1.

            `phonebook_id` (str): ID of phonebook.
        """

        self.validate_authentication()
        data = RequestData(
            url=FETCH_CONTACTS.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                page=page,
                phonebook_id=phonebook_id
            ),
            type=RequestType.get,
        )
        return make_request(data=data)
