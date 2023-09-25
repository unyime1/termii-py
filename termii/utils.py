from typing import Dict
import random
import string

import requests

from termii.schemas.shared import RequestData, RequestType


def make_request(data: RequestData) -> Dict:
    """Handle requests dispatch."""
    if data.type == RequestType.post:
        response = requests.post(
            url=data.url, json=data.payload if data.payload else {}
        )
        return response.json()

    elif data.type == RequestType.get:
        response = requests.get(url=data.url)
        return response.json()

    elif data.type == RequestType.patch:
        response = requests.patch(
            url=data.url, json=data.payload if data.payload else {}
        )
        return response.json()

    elif data.type == RequestType.delete:
        response = requests.delete(url=data.url)
        return response.json()


def get_random_string(count) -> str:
    """Generate random strings."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(count))


def get_random_numbers(count) -> str:
    characters = string.digits
    return "".join(random.choice(characters) for _ in range(count))
