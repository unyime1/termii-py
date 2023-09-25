FETCH_PHONEBOOKS = (
    "{TERMII_ENDPOINT_URL}/api/phonebooks?api_key={TERMII_API_KEY}&page={page}"
)
CREATE_PHONEBOOK = "{TERMII_ENDPOINT_URL}/api/phonebooks"
UPDATE_PHONEBOOK = "{TERMII_ENDPOINT_URL}/api/phonebooks/{phonebook_id}"
DELETE_PHONEBOOK = (
    "{TERMII_ENDPOINT_URL}/api/phonebooks/{phonebook_id}?api_key={TERMII_API_KEY}"  # noqa
)
