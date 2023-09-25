from typing import Optional, Dict
from enum import Enum

from pydantic import BaseModel


class RequestType(str, Enum):
    post = "post"
    get = "get"
    patch = "patch"
    delete = "delete"


class RequestData(BaseModel):
    url: str
    payload: Optional[Dict] = None
    type: RequestType
