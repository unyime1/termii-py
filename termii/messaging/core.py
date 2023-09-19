from typing import Dict, Optional, List

from termii.auth import Client
from termii.messaging.schemas import (
    RequestData,
    RequestType,
    MessagingChannel
)
from termii.messaging.endpoints import (
    FETCH_SENDER_ID,
    REQUEST_SENDER_ID,
    SEND_MESSAGE
)
from termii.utils import make_request


class Messaging(Client):
    """
    Base class for core messaging APIs.
    """
    def fetch_sender_id(self, page: Optional[int] = 1) -> Dict:
        """
        `Documentation`: https://developers.termii.com/sender-id

        Fetch sender IDs from API.

        Args:
            `page` (int, None): Page to fetch. Starts from 1.

        Returns:
            Dict.
        """
        self.validate_authentication()

        # Prepare request.
        data = RequestData(
            url=FETCH_SENDER_ID.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL,
                TERMII_API_KEY=self.TERMII_API_KEY,
                data_page=page,
            ),
            type=RequestType.get,
        )
        return make_request(data=data)

    def request_sender_id(
        self,
        sender_id: str,
        usecase: str,
        company: str,
        api_key: str,
        endpoint_url: str,
    ) -> Dict:
        """
        `Documentation`: https://developers.termii.com/sender-id

        Request new sender ID from API.

        Args:
            `sender_id` (str): Represents the ID of the sender which can be
            alphanumeric or numeric. Alphanumeric sender ID length
            should be between 3 and 11 characters (Example:CompanyName)

            `usecase` (str): A sample of the type of message sent.

            `company` (str): Represents the name of the company with the
                            sender ID.

            `api_key` (str): API key from Termii dashboard.

            `endpoint_url` (str): Endpoint url from dashboard.
            E.g https://api.ng.termii.com
        
        Returns:
            Dict.
        """
        payload = dict(
            api_key=api_key,
            sender_id=sender_id,
            usecase=usecase,
            company=company,
        )
        request_data = RequestData(
            url=REQUEST_SENDER_ID.format(TERMII_ENDPOINT_URL=endpoint_url),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def send_message(
        self,
        receivers: List[str],
        channel: MessagingChannel,
        text: str,
        media_url: Optional[str],
        media_caption: Optional[str],
    ) -> Dict:
        """
        `Documentation`: https://developers.termii.com/messaging-api

        Send text messages to their customers across different messaging channels.

        Args:
            `receivers` (List[str]): Accepts a list of receipient phone numbers in
            international format. An example is [2348364528908]. Note the absence of
            +.

            `channel` (MessagingChannel): This is the route through which the message is sent.
            It is either `MessagingChannel.dnd`, `MessagingChannel.whatsapp`,
            or `MessagingChannel.generic`.

            `media` (Optional[str]): This is a media object, it is only available for
            `MessagingChannel.whatsapp` channel.

            `media_url` (Optional[str]): The url to the file resource. Only the following
            formats are supported: JPG, JPEG, PNG, MP3, OGG, AMR, PDF, MP4

            `media_caption` (Optional[str]): The caption that should be added to the media.
        
        Returns:
            Dict.
        """
        self.validate_authentication()

        # Validate properties.
        if media_url:
            if channel != MessagingChannel.whatsapp:
                raise ValueError(f"This argument is only allowed with {MessagingChannel.whatsapp.value} channel.")
        
        if len(receivers) >= 100:
            raise ValueError(f"You cannot send to more than 100 mobile numbers.")

        # Prepare payload.
        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["from"] = self.TERMII_SENDER_ID
        payload["to"] = receivers
        payload["type"] = "plain"
        payload["channel"] = channel.value
        payload["sms"] = text

        if media_url:
            payload["media"] = dict(
                media_url=media_url,
                caption=media_caption
            )

        # Make request.
        request_data = RequestData(
            url=SEND_MESSAGE.format(TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)
