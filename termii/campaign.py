import re

from typing import Dict, Optional
from datetime import datetime

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
    SEND_CAMPAIGN,
    FETCH_CAMPAIGNS,
    FETCH_CAMPAIGN_HISTORY,
)
from termii.schemas.messaging import MessagingChannel


class Campaign(Client):
    """
    Handle operations related to phonebook.
    """

    def validate_phonebook_name(self, name: str):
        """Validate that phonebook name contains only letters and numbers."""
        pattern = "^[a-zA-Z0-9]+$"
        if not re.match(pattern, name):
            raise ValueError(
                "Phonebook name must contain only letters and numbers."
            )

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
        self.validate_phonebook_name(name)

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
        self.validate_phonebook_name(name)

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

    def send_campaign(
        self,
        message: str,
        country_code: str,
        phonebook_id: str,
        campaign_type: Optional[str] = "personalized",
        message_type: Optional[str] = "plain",
        schedule_time: Optional[datetime] = None,
        channel: Optional[MessagingChannel] = MessagingChannel.generic,
    ) -> Dict:
        """
        `Documentation`: https://developers.termii.com/campaign#send-a-campaign

        Send campaign message to phonebook.

        Args:
            `message` (str): Text message to send.

            `country_code` (str): Represents short numeric geographical
                codes developed to represent countries (Example: 234 ).

            `phonebook_id` (str): Id of phonebook to send to.

            `campaign_type` (Optional[str]): Represents type of campaign.

            `message_type` (Optiional[str]): The type of message that is sent,
                which is a plain message.

            `schedule_time` (Optional[datetime]): Needed if message is scheduled.
        """  # noqa

        # Data validation.
        self.validate_authentication()

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["sender_id"] = self.TERMII_SENDER_ID
        payload["country_code"] = country_code
        payload["message"] = message
        payload["channel"] = channel.value
        payload["message_type"] = message_type
        payload["phonebook_id"] = phonebook_id
        payload["campaign_type"] = campaign_type

        if schedule_time:
            payload["schedule_sms_status"] = "scheduled"
            payload["schedule_time"] = str(schedule_time)

        request_data = RequestData(
            url=SEND_CAMPAIGN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def fetch_campaigns(self, page: Optional[int] = 1) -> Dict:
        """
        `Documentation`: https://developers.termii.com/campaign#fetch-campaigns

        Get all campaigns.

        Args:
            `page` (Optional[int]): Campaign page.
        """  # noqa

        # Data validation.
        self.validate_authentication()
        request_data = RequestData(
            url=FETCH_CAMPAIGNS.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                page=page,
            ),
            type=RequestType.get,
        )
        return make_request(data=request_data)

    def fetch_campaign_history(
        self, campaign_id: str, page: Optional[int] = 1
    ) -> Dict:
        """
        `Documentation`: https://developers.termii.com/campaign#fetch-campaign-history

        Get single campaign history.

        Args:
            `page` (Optional[int]): Campaign page.
        """  # noqa

        # Data validation.
        self.validate_authentication()
        request_data = RequestData(
            url=FETCH_CAMPAIGN_HISTORY.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                page=page,
                campaign_id=campaign_id,
            ),
            type=RequestType.get,
        )
        return make_request(data=request_data)
