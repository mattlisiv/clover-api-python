import requests


class AppService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Apps

    # BillingInfo
    def get_merchant_billing_info(self, app_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/apps/' + app_id + '/merchants/' + self.merchant_id + '/billing_info',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Metereds
    def create_app_billing_metered_event(self, app_id, metered_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/apps/' + app_id + '/merchants/' + self.merchant_id + '/metereds/' + metered_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_app_metered_billing_event(self, app_id, metered_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/apps/' + app_id + '/merchants/' + self.merchant_id + '/metereds/' + metered_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Events
    def get_app_billing_metered_event(self, app_id, metered_id, event_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/apps/' + app_id + '/merchants/' + self.merchant_id + '/metereds/'
            + metered_id + '/events/' + event_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def delete_app_billing_metered_event(self, app_id, metered_id, event_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/apps/' + app_id + '/merchants/' + self.merchant_id + '/metereds/'
            + metered_id + '/events/' + event_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()
