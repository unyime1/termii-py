# Termii-py

Super easy SDK for [Termii](https://termii.com/) SMS APIs.

## Installation

Install using `pip install -U termii-py`.

## Simple Examples

```python
from termii.token import Token
from termii.schemas.token import TokenType

token_client = Token()
token_client.authenticate_from_env()
response = token_client.send_token(
    message_type=TokenType.ALPHANUMERIC,
    receiver="2348152436475",
)
print(response)

```

```python
from termii.messaging import Messaging

messaging_client = Messaging()
messaging_client.authenticate_from_env()

receivers = ["2348152436475", "2347153436435"]
response = messaging_client.send_message(
    receivers=receivers,
    text="Hello all. Thanks for visiting."
)
print(response)
```

```python
from termii.campaign import Campaign

campaign_client = Campaign()
campaign_client.authenticate_from_env()
response = campaign_client.create_phonebook(
    name="Test", description="Test description."
)
print(response)
```

## Authentication.
There are two ways of authenticating requests:
1. With env variables:
To authenticate with environment variables set `TERMII_API_KEY`, `TERMII_ENDPOINT_URL`, `TERMII_SENDER_ID` to your termii api key, endpoint url and sender ID respectively. Then call client.authenticate_from_env()

Example:
```python
import os

from termii.campaign import Campaign

os.environ["TERMII_API_KEY"] = "ukwiwe4642eh"
os.environ["TERMII_ENDPOINT_URL"] = "https://api.ng.termii.com"
os.environ["TERMII_SENDER_ID"] = "Test"

campaign_client = Campaign()
campaign_client.authenticate_from_env()
```

2. A second method is to pass in the credentials directly. For that call `authenticate_direct()` on all clients and pass-in the credentials.


## Contributing

For guidance on setting up a development environment and how to make a
contribution to termii-py, see
[Contributing to Termii-py](CONTRIBUTING.md).


## Reporting a Security Vulnerability

Please send a private mail to `lordunyime@gmail.com` if you discover any security vulnerability. I'll be happy to work with you on a fix.