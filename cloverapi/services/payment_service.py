import requests


class PaymentService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Payments
    def get_payments(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/payments/',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_payments_by_order(self, order_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/payments/',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_payments_by_employee(self, employee_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/payments/',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_payment_by_id(self, payment_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/payments/' + payment_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def update_payment_by_id(self, payment_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/payments/' + payment_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Refunds
    def get_refunds(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/refunds',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_refund_by_id(self, refund_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/refunds/' + refund_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Credits
    def get_credits(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/credits',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_credit_by_id(self, credit_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/credits/' + credit_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Credit Refunds
    def get_credit_refunds(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/credit_refunds',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_credit_refund_by_id(self, credit_refund_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/credit_refunds/' + credit_refund_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()