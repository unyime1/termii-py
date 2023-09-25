from termii.campaign import Campaign
from tests.test_data.campaign import get_phonebook


class TestSenderID:
    def test_get_phonebooks(self, test_environments, mock_get_phonebook):
        """Test fetch of phonebooks"""
        campaign_client = Campaign()
        campaign_client.authenticate_from_env()
        phonebooks = campaign_client.get_phonebooks()

        print(phonebooks)
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
