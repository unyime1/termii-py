from enum import Enum


class TokenType(str, Enum):
    NUMERIC = "NUMERIC"
    ALPHANUMERIC = "ALPHANUMERIC"


class MessagingChannel(str, Enum):
    generic = "generic"
    dnd = "dnd"
    whatsapp = "whatsapp"
    email = "email"
