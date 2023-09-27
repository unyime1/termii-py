import uuid
import csv
import os

import pytest

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

    def test_add_multiple_contact(
        self, test_environments, mock_add_multi_contacts
    ):
        """Test add multiple contacts to phonebook."""
        data = [
            ["phone_number", "first_name"],
            ["534746580", "Alex"],
            ["645638576", "Titus"],
        ]
        file_name = "contacts.csv"

        with open(file_name, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)

        contact_client = Contacts()
        contact_client.authenticate_from_env()
        response = contact_client.add_multiple_contacts(
            phonebook_id=str(uuid.uuid4()),
            country_code="234",
            filename=file_name,
        )
        assert (
            "Your list is being uploaded in the background."
            in response.get("message")
        )
        os.remove(file_name)

    def test_add_multiple_contact_fail(
        self, test_environments, mock_add_multi_contacts
    ):
        """Test add multiple contacts to phonebook."""
        data = [
            ["phone_number", "first_name"],
            ["534746580", "Alex"],
            ["645638576", "Titus"],
        ]
        file_name = "contacts.da"

        with open(file_name, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)

        contact_client = Contacts()
        contact_client.authenticate_from_env()
        with pytest.raises(ValueError) as value_error:
            contact_client.add_multiple_contacts(
                phonebook_id=str(uuid.uuid4()),
                country_code="234",
                filename=file_name,
            )
            assert str(value_error.value) == "This file type is not supported."
        os.remove(file_name)

    def test_delete_contact(self, test_environments, mock_delete_contact):
        """Test delete contact"""
        contact_client = Contacts()
        contact_client.authenticate_from_env()
        response = contact_client.delete_contact(contact_id=str(uuid.uuid4()))
        print(response)
        assert response["message"] == "Contact deleted successfully"
