from typing import Optional, Dict

from pydantic import EmailStr

from termii.auth import Client
from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.token import (
    SEND_TOKEN,
    SEND_EMAIL_TOKEN,
    SEND_VOICE_TOKEN,
    VERIFY_TOKEN,
    IN_APP_TOKEN,
)
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

    def validate_numerical(self, code: int) -> None:
        """Validate that code is an integer."""
        print(isinstance(code, int))
        if not isinstance(code, int):
            raise ValueError("Code must be numerical.")

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
        self.validate_authentication()
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
        method.

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
            url=SEND_VOICE_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def voice_call(self, phone_number: str, code: int) -> Dict:
        """
        The voice call API enables you to send messages
        from your application through our voice channel
        to a phone number. Only one-time-passwords (OTP)
        are allowed for now and these OTPs can not be
        verified using our Verify Token API.

        Documentation: https://developers.termii.com/voice-call

        Args:
            `phone_number` (str): The destination phone number.
            Phone number must be in the international
            format (Example: 23490126727)

            `code` (int): Example: 3344. The code you want
            your users to receive. It has to be numeric
            and length must be between 4 and 8 digits.
        """
        self.validate_authentication()
        self.validate_pin_length(pin_length=len(str(code)))
        self.validate_numerical(code=code)

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["phone_number"] = phone_number
        payload["code"] = code

        request_data = RequestData(
            url=SEND_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def email_token(
        self, email_address: EmailStr, code: str, email_configuration_id: str
    ) -> Dict:
        """
        The email token API enables you to send one-time-passwords
        from your application through our email channel
        to an email address. Only one-time-passwords (OTP)
        are allowed for now and these OTPs can not be
        verified using our Verify Token API.

        Documentation: https://developers.termii.com/email-token

        Args:
            `email_address` (str): Represents the email address
            you are sending to (Example: test@termii.com).

            `code` (str): Represents the OTP sent to the
            email address.

            `email_configuration_id` (str): This is represents
            the email configuration you have added on
            your Termii dashboard. It can be found
            on your Termii dashboard.
        """
        self.validate_authentication()
        self.validate_pin_length(pin_length=len(str(code)))

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["email_address"] = email_address
        payload["code"] = code
        payload["email_configuration_id"] = email_configuration_id

        request_data = RequestData(
            url=SEND_EMAIL_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def verify_token(self, pin_id: str, pin: str) -> Dict:
        """
        Verify token API, checks tokens sent to customers and
        returns a response confirming the status of the token.
        A token can either be confirmed as verified or expired
        based on the timer set for the token.

        Documentation: https://developers.termii.com/verify-token

        Args:
            `pin_id` (str): ID of the PIN sent
                (Example: "c8dcd048-5e7f-4347-8c89-4470c3af0b")

            `pin` (str): The PIN code (Example: "195558").
        """
        self.validate_authentication()

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["pin_id"] = pin_id
        payload["pin"] = pin

        request_data = RequestData(
            url=VERIFY_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)

    def in_app_token(
        self,
        pin_type: TokenType,
        phone_number: str,
        pin_attempts: Optional[int] = 1,
        pin_time_to_live: Optional[int] = 15,
        pin_length: Optional[int] = 4,
    ) -> Dict:
        """
        The send token API allows businesses trigger one-time-passwords (OTP)
        across any available messaging channel on Termii. One-time-passwords
        created are generated randomly and there's an option to set an expiry
        time.

        Args:
            `pin_type` (TokenType): Type of pin code that will be generated
            and sent as part of the OTP message.

            `phone_number` (str): Represents the destination phone number.
            Phone number must be in the international format
            (Example: 23490126727)

            `pin_attempts` (int): Represents the number of times the PIN
            can be attempted before expiration. It has a minimum of
            one attempt.

            `pin_time_to_live` (int): Represents how long the PIN is
            valid before expiration. The time is in minutes.
            The minimum time value is 0 and the maximum time value is 60

            `pin_length` (int): The length of the PIN code. It has a
            minimum of 4 and maximum of 8.
        """
        self.validate_authentication()
        self.validate_pin_attempts(attempts=pin_attempts)
        self.validate_pin_time_to_live(pin_time_to_live=pin_time_to_live)
        self.validate_pin_length(pin_length=pin_length)

        payload = {}
        payload["api_key"] = self.TERMII_API_KEY
        payload["pin_attempts"] = pin_attempts
        payload["pin_time_to_live"] = pin_time_to_live
        payload["pin_length"] = pin_length
        payload["pin_type"] = pin_type.value
        payload["phone_number"] = phone_number

        request_data = RequestData(
            url=IN_APP_TOKEN.format(
                TERMII_ENDPOINT_URL=self.TERMII_ENDPOINT_URL
            ),
            payload=payload,
            type=RequestType.post,
        )
        return make_request(data=request_data)
