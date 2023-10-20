import uuid

from termii.campaign import Campaign
from tests.test_data.campaign import (
    get_phonebook,
    fetch_campaigns,
    fetch_campaign_history,
)


class TestPhonebook:
    def test_get_phonebooks(self, test_environments, mock_get_phonebook):
        """Test fetch of phonebooks"""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        phonebooks = campaign_client.get_phonebooks()

        assert len(phonebooks.get("data")) == len(get_phonebook.get("data"))
        assert (
            phonebooks.get("data")[0]["id"]
            == get_phonebook.get("data")[0]["id"]
        )
        assert (
            phonebooks.get("data")[0]["name"]
            == get_phonebook.get("data")[0]["name"]
        )
        assert (
            phonebooks.get("data")[0]["last_updated"]
            == get_phonebook.get("data")[0]["last_updated"]
        )

    def test_create_phonebook(self, test_environments, mock_create_phonebook):
        """Create phonebook."""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        response = campaign_client.create_phonebook(
            name="Test", description="Test description."
        )
        response.get("message") == "Phonebook added successfully"

    def test_update_phonebook(self, test_environments, mock_update_phonebook):
        """Test Update phonebook."""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        response = campaign_client.update_phonebook(
            name="Test2",
            description="Test description.",
            phonebook_id=str(uuid.uuid4()),
        )
        response.get("message") == "Phonebook updated successfully"

    def test_delete_phonebook(self, test_environments, mock_delete_phonebook):
        """Test delete phonebook."""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        data = campaign_client.delete_phonebook(phonebook_id=str(uuid.uuid4()))
        assert data.get("message") == "Phonebook deleted successfully"

    def test_send_campaign(
        self, test_environments, mock_send_campaign_contact
    ):
        """Test send campaign."""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        data = campaign_client.send_campaign(
            message="Test",
            country_code="234",
            phonebook_id=str(uuid.uuid4()),
        )
        assert data.get("message") == "Your campaign has been scheduled"

    def test_fetch_campaigns(self, test_environments, mock_fetch_campaigns):
        """Test send campaign."""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        data = campaign_client.fetch_campaigns(page=1)
        assert len(data.get("data")) == len(fetch_campaigns.get("data"))

    def test_fetch_campaign_history(
        self, test_environments, mock_fetch_campaign_history
    ):
        """Test fetch campaign histiry."""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        data = campaign_client.fetch_campaign_history(
            page=1, campaign_id=str(uuid.uuid4())
        )
        assert len(data.get("data")) == len(fetch_campaign_history.get("data"))
