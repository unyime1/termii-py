# flake8: noqa

FETCH_PHONEBOOKS = (
    "{TERMII_ENDPOINT_URL}/api/phonebooks?api_key={TERMII_API_KEY}&page={page}"
)
CREATE_PHONEBOOK = "{TERMII_ENDPOINT_URL}/api/phonebooks"
UPDATE_PHONEBOOK = "{TERMII_ENDPOINT_URL}/api/phonebooks/{phonebook_id}"
DELETE_PHONEBOOK = "{TERMII_ENDPOINT_URL}/api/phonebooks/{phonebook_id}?api_key={TERMII_API_KEY}"
SEND_CAMPAIGN = "{TERMII_ENDPOINT_URL}/api/sms/campaigns/send"
FETCH_CAMPAIGNS = "{TERMII_ENDPOINT_URL}/api/sms/campaigns?api_key={TERMII_API_KEY}&page={page}"
FETCH_CAMPAIGN_HISTORY = "{TERMII_ENDPOINT_URL}/api/sms/campaigns/{campaign_id}?api_key={TERMII_API_KEY}&page={page}"
