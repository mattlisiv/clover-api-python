import requests


class CustomerService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Customers

    # CustomersCSV
    def get_customers_csv(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/customers.csv/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Customers
    def get_customers(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/customers/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def create_customer(self, customer):
        # Define Payload
        payload = customer
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/',
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def get_customer_by_id(self, customer_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/customers/' + customer_id,
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def update_customer_by_id(self, customer):
        # Define Payload
        payload = customer
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/' + customer["id"],
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_customer_by_id(self, customer_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/customers/' + customer_id,
                            auth=self.auth, timeout=30, params=payload)
        return r.json()

    # PhoneNumbers
    def create_customer_phone_number_by_id(self, customer_id, phone_number):
        # Define Payload
        payload = phone_number
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/phone_numbers', auth=self.auth, timeout=30, json=payload)
        return r.json()

    def update_customer_phone_number_by_id(self, customer_id, phone_number):
        # Define Payload
        payload = phone_number
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/phone_numbers/' + phone_number["id"], auth=self.auth, timeout=30,
                          json=payload)
        return r.json()

    def delete_customer_phone_number_by_id(self, customer_id, phone_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                            + customer_id + '/phone_numbers/' + phone_id, auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Email Addresses
    def create_customer_email_address_by_id(self, customer_id, email):
        # Define Payload
        payload = email
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/email_addresses', auth=self.auth, timeout=30, json=payload)
        return r.json()

    def update_customer_email_address_by_id(self, customer_id, email):
        # Define Payload
        payload = email
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/email_addresses/' + email["id"],
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_customer_email_address_by_id(self, customer_id, email_address_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                            + customer_id + '/email_addresses/' + email_address_id,
                            auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Addresses
    def create_customer_address_by_id(self, customer_id, address):
        # Define Payload
        payload = address
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/addresses', auth=self.auth, timeout=30, json=payload)
        return r.json()

    def update_customer_address_by_id(self, customer_id, address):
        # Define Payload
        payload = address
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/addresses/' + address["id"], auth=self.auth, timeout=30, params=payload)
        return r.json()

    def delete_customer_address_by_id(self, customer_id, address_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                            + customer_id + '/addresses/' + address_id, auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Cards
    def create_customer_card_by_id(self, customer_id, card):
        # Define Payload
        payload = card
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/cards', auth=self.auth, timeout=30, json=payload)
        return r.json()

    def update_customer_card_by_id(self, customer_id, card):
        # Define Payload
        payload = card
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/cards/' + card["id"], auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_customer_card_by_id(self, customer_id, card_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                            + customer_id + '/cards/' + card_id, auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Metadata
    def create_customer_note_by_id(self, customer_id, customer_metadata):
        # Define Payload
        payload = customer_metadata
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/customers/'
                          + customer_id + '/metadata', auth=self.auth, timeout=30, json=payload)
        return r.json()