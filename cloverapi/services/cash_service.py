import requests


class CashService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Cash Events
    def get_cash_events(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/cash_events/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def get_cash_events_by_employee(self, employee_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/cash_events',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def get_cash_events_by_device(self, device_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/devices/' + device_id + '/cash_events',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()