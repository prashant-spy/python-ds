import pytest
import requests


def get_oauth2_token(client_id, client_secret, token_url):
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(token_url, data=data)
    response.raise_for_status()
    return response.json()['access_token']


@pytest.fixture.mark.parameterize("input", "output", [('test', 9), ('test2', 3)])
def oauth2_token():
    client_id = 'your-client-id'
    client_secret = 'your-client-secret'
    token_url = 'https://your-auth-server.com/oauth2/token'
    return get_oauth2_token(client_id, client_secret, token_url)


def test_authenticated_request(oauth2_token):
    headers = {
        'Authorization': f'Bearer {oauth2_token}'
    }
    response = requests.get('https://api.yourservice.com/protected-resource', headers=headers)
    assert response.status_code == 200
