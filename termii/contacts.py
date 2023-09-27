from typing import Dict, Optional

import requests
from pydantic import EmailStr

from termii.auth import Client
from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.contacts import (
    FETCH_CONTACTS,
    ADD_CONTACT,
    DELETE_CONTACT,
)


class Contacts(Client):
    def get_contacts(self, phonebook_id: str, page: Optional[int] = 1) -> Dict:
        """
        Get all contacts on phonebook.
        Docs: https://developers.termii.com/contacts

        Args:
            `page` (int): Page to return. Starts at 1.

            `phonebook_id` (str): ID of phonebook.
        """  # noqa

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
        """  # noqa

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

    def validate_contact_file(self, file_path: str) -> None:
        """Validate that file has an accepted extention."""
        allowed_extensions = ["txt", "xlsx", "csv"]
        if file_path.split(".")[-1] not in allowed_extensions:
            raise ValueError("This file type is not supported.")

    def add_multiple_contacts(
        self, filename: str, country_code: str, phonebook_id: str
    ) -> Dict:
        """
        Add multiple contacts to phonebook
        Docs: https://developers.termii.com/contacts#add-multiple-contacts-to-phonebook

        Args:
            `phonebook_id` (str): ID of phonebook.

            `phone_number` (str): Phone number of the contact.

            `country_code` (str): Represents short numeric
                geographical codes developed to represent countries (Example: 234 ).

            `file_path` (str): File containing the list of contacts you want to
                add to your phonebook. Supported files include : 'txt', 'xlsx', and 'csv'.
        """  # noqa

        self.validate_authentication()
        self.validate_contact_file(filename)

        payload = {
            "country_code": country_code,
            "api_key": self.TERMII_API_KEY,
        }
        files = [("contact_file", (f"{filename}", "rb"), "text/csv")]

        response = requests.post(
            ADD_CONTACT.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                phonebook_id=phonebook_id,
            ),
            data=payload,
            files=files,
        )
        return response.json()

    def delete_contact(self, contact_id: str) -> Dict:
        """
        Get all contacts on phonebook.
        Docs: https://developers.termii.com/contacts#delete-phonebook

        Args:
            `contact_id` (str): ID of contact.
        """  # noqa

        self.validate_authentication()
        data = RequestData(
            url=DELETE_CONTACT.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                contact_id=contact_id,
            ),
            type=RequestType.delete,
        )
        return make_request(data=data)
