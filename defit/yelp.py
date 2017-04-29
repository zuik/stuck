import requests
from urllib.error import HTTPError

CLIENT_ID = "0Xdf4oHsQwS8wkoi0qRd1g"
CLIENT_SECRET = "M1UMC49hwVpdJe0m3WbHEWg4Vgn6ULAHJYF0pNiecRugIe0bCg2nxcWCXQoGsgoH"


def obtain_bearer_token(host, path):
    # From Yelp's sample code on Github
    """Given a bearer token, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        str: OAuth bearer token, obtained using client_id and client_secret.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    assert CLIENT_ID, "Please supply your client_id."
    assert CLIENT_SECRET, "Please supply your client_secret."
    data = urlencode({
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    })
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
    }
    response = requests.request('POST', url, data=data, headers=headers)
    bearer_token = response.json()['access_token']
    return bearer_token
