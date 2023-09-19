from enum import Enum
from typing import Optional, Dict

from pydantic import BaseModel


class RequestType(str, Enum):
    post = "post"
    get = "get"


class RequestData(BaseModel):
    url: str
    payload: Optional[Dict] = None
    type: RequestType


class MessagingChannel(str, Enum):
    generic = "generic"
    dnd = "dnd"
    whatsapp = "whatsapp"


class MessageDistributionType(str, Enum):
    simple = "simple"
    bulk = "bulk"
