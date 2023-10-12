from typing import Optional, Dict

from termii.auth import Client
from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.token import SEND_TOKEN
from termii.schemas.token import TokenType, MessagingChannel


class Token(Client):
    """
    Base class for token APIs.

    Documentation: https://developer.termii.com/token
    """

    def validate_pin_attempts(self, attempts: int) -> None:
        """Validate pin attempts."""
        if attempts < 1:
            raise ValueError("Pin attempts must be atleast 1.")

    def validate_pin_time_to_live(self, pin_time_to_live: int) -> None:
        """Validate pin time to live."""
        if pin_time_to_live < 0 or pin_time_to_live > 60:
            raise ValueError("pin_time_to_live must be between 0 and 60.")

    def validate_pin_length(self, pin_length: int) -> None:
        """Validate how long a pin should be."""
        if pin_length < 4 or pin_length > 8:
            raise ValueError("pin_length must be between 4 and 8.")

    def validate_message_text(
        self, pin_placeholder: str, message_text: str
    ) -> None:
        """Validate entered message."""
        if pin_placeholder not in message_text:
            raise ValueError("Your pin_placeholder must be in message_text.")

    def send_token(
        self,
        message_type: TokenType,
        receiver: str,
        channel: Optional[MessagingChannel] = MessagingChannel.generic,
        pin_attempts: Optional[int] = 1,
        pin_time_to_live: Optional[int] = 15,
        pin_length: Optional[int] = 4,
        pin_placeholder: Optional[str] = "< 1234 >",
        message_text: Optional[str] = "Your pin is < 1234 >",
    ) -> Dict:
        """
        The send token API allows businesses trigger one-time-passwords (OTP)
        across any available messaging channel on Termii. One-time-passwords
        created are generated randomly and there's an option to set an expiry
        time.

        Args:
            `message_type` (TokenType): Type of message that will be generated
            and sent as part of the OTP message.

            `receiver` (str): Represents the email address if the channel
            is set to email (Example: testshola@termii.com). It represents
            the destination phone number if other channels are selected.
            Phone number must be in the international format.
            (Example: 23490126727)

            `channel` (MessagingChannel): This is the route through which
            the message is sent. It is either dnd, WhatsApp, or generic
            or email.

            `pin_attempts` (int): Represents the number of times the PIN
            can be attempted before expiration. It has a minimum of
            one attempt.

            `pin_time_to_live` (int): Represents how long the PIN is
            valid before expiration. The time is in minutes.
            The minimum time value is 0 and the maximum time value is 60

            `pin_length` (int): The length of the PIN code. It has a
            minimum of 4 and maximum of 8.

            `pin_placeholder` (str): PIN placeholder. Right before
            sending the message, PIN code placeholder will be replaced
            with generate PIN code. Example: "< 1234 >"

            `message_text` (str): Text of a message that would be sent
            to the destination phone number. Example: "Your pin is < 1234 >"
        """
        self.validate_pin_attempts(attempts=pin_attempts)
        self.validate_pin_time_to_live(pin_time_to_live=pin_time_to_live)
        self.validate_pin_length(pin_length=pin_length)
        self.validate_message_text(
            pin_placeholder=pin_placeholder, message_text=message_text
        )

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["message_type"] = message_type.value
        payload["to"] = receiver
        payload["from"] = self.TERMII_SENDER_ID
        payload["channel"] = channel.value
        payload["pin_attempts"] = pin_attempts
        payload["pin_time_to_live"] = pin_time_to_live
        payload["pin_length"] = pin_length
        payload["pin_placeholder"] = pin_placeholder
        payload["message_text"] = message_text
        payload["pin_type"] = message_type.value

        request_data = RequestData(
            url=SEND_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def send_voice_token(
        self,
        phone_number: str,
        pin_attempts: Optional[int] = 1,
        pin_time_to_live: Optional[int] = 15,
        pin_length: Optional[int] = 4,
    ) -> Dict:
        """
        The voice token API enables you to generate and trigger
        one-time passwords (OTP) through the voice channel to a
        phone number. OTPs are generated and sent to the phone
        number and can only be verified using our Verify
        Token API.

        Args:
            `phone_number` (str): The destination phone number.
            Phone number must be in the international
            format (Example: 23490126727)

            `pin_attempts` (int): Represents the number of times the PIN
            can be attempted before expiration. It has a minimum of
            one attempt.

            `pin_time_to_live` (int): Represents how long the PIN is
            valid before expiration. The time is in minutes.
            The minimum time value is 0 and the maximum time value is 60

            `pin_length` (int): The length of the PIN code. It has a
            minimum of 4 and maximum of 8.
        """
        self.validate_pin_attempts(attempts=pin_attempts)
        self.validate_pin_time_to_live(pin_time_to_live=pin_time_to_live)
        self.validate_pin_length(pin_length=pin_length)

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["phone_number"] = phone_number
        payload["pin_attempts"] = pin_attempts
        payload["pin_time_to_live"] = pin_time_to_live
        payload["pin_length"] = pin_length

        request_data = RequestData(
            url=SEND_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)
