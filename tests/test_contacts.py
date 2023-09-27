import uuid

from termii.contacts import Contacts
from tests.test_data.campaign import get_contacts, add_contact


class TestContacts:
    def test_get_contacts(self, test_environments, mock_get_contacts):
        """Test fetch of contacts from phonebook"""
        contact_client = Contacts()
        contact_client.authenticate_from_env()
        contacts = contact_client.get_contacts(phonebook_id=str(uuid.uuid4()))

        assert len(contacts.get("data")) == len(get_contacts.get("data"))

    def test_add_contact(self, test_environments, mock_add_contacts):
        """Test add contact to phonebook"""
        contact_client = Contacts()
        contact_client.authenticate_from_env()
        response = contact_client.add_single_contact(
            phonebook_id=str(uuid.uuid4()),
            phone_number="35475869",
            country_code="234",
            email_address="test@gmail.com",
            first_name="Unyime",
            last_name="Etim",
            company="Termii",
        )
        assert response["data"]["id"] == add_contact["data"]["id"]
