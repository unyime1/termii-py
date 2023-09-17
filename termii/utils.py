from typing import Dict

import requests

from termii.messaging.schemas import RequestData, RequestType


def make_request(data: RequestData) -> Dict:
    """Handle requests dispatch."""
    match data.type:
        case RequestType.post:
            response = requests.post(
                url=data.url, json=data.payload if data.payload else {}
            )
            return response.json()

        case RequestType.get:
            response = requests.get(url=data.url)
            return response.json()
