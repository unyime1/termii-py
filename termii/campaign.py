from typing import Dict, Optional

from termii.auth import Client

from termii.schemas.shared import (
    RequestData,
    RequestType,
)
from termii.utils import make_request
from termii.endpoints.campaign import FETCH_PHONEBOOKS


class Campaign(Client):
    """
    Handle operations related to phonebook.
    """

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
