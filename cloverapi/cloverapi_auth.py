from requests.auth import AuthBase


class CloverApiAuth(AuthBase):
    # Provided by clover: https://docs.clover.com/build/oauth-2-0/
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, request):
        request.headers.update(get_auth_headers(self.api_key))
        return request


def get_auth_headers(api_key):
    return {
        'Content-Type': 'Application/JSON',
        'Authorization': 'Bearer ' + api_key
    }
