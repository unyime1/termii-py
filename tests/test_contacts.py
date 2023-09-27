import uuid

from termii.contacts import Contacts
from tests.test_data.campaign import get_contacts


class TestContacts:
    def test_get_contacts(self, test_environments, mock_get_contacts):
        """Test fetch of contacts from phonebook"""
        contact_client = Contacts()
        contact_client.authenticate_from_env()
        contacts = contact_client.get_contacts(phonebook_id=str(uuid.uuid4()))

        assert len(contacts.get("data")) == len(get_contacts.get("data"))

