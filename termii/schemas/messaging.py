from enum import Enum


class MessagingChannel(str, Enum):
    generic = "generic"
    dnd = "dnd"
    whatsapp = "whatsapp"


class MessageDistributionType(str, Enum):
    simple = "simple"
    bulk = "bulk"
