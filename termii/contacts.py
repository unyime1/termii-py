from typing import Dict, Optional

from pydantic import EmailStr

from termii.auth import Client
from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.contacts import FETCH_CONTACTS, ADD_CONTACT


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
                phonebook_id=phonebook_id,
            ),
            type=RequestType.get,
        )
        return make_request(data=data)

    def add_single_contact(
        self,
        phonebook_id: str,
        phone_number: str,
        country_code: str,
        email_address: Optional[EmailStr] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
    ) -> Dict:
        """
        Get all contacts on phonebook.
        Docs: https://developers.termii.com/contacts#add-single-contacts-to-phonebook

        Args:
            `phonebook_id` (str): ID of phonebook.

            `phone_number` (str): Phone number of the contact.

            `country_code` (str): Represents short numeric
                geographical codes developed to represent countries (Example: 234 ).

            `email_address` (str | None): email address of the contact.

            `first_name` (str | None): First name of contact.

            `last_name` (str | None): Last name of contact.

            `company` (str | None): Company of contact.
        """

        self.validate_authentication()
        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["phone_number"] = phone_number
        payload["country_code"] = country_code
        payload["email_address"] = email_address
        payload["first_name"] = first_name
        payload["last_name"] = last_name
        payload["company"] = company

        cleaned_payload = {
            key: value for key, value in payload.items() if value is not None
        }

        data = RequestData(
            url=ADD_CONTACT.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                phonebook_id=phonebook_id,
            ),
            type=RequestType.post,
            payload=cleaned_payload,
        )
        return make_request(data=data)
