import requests


class OrderService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Orders
    def get_orders(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_order(self, order):
        # Define Payload
        payload = order
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def get_order_by_id(self, order_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def update_order_by_id(self, order):
        # Define Payload
        payload = order
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_order_by_id(self, order_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Discounts
    def get_discounts_for_order(self, order_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/discounts',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_discount_for_order(self, order_id, discount):
        # Define Payload
        payload = discount
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/discounts',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_discount_for_order(self, order_id, discount_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/discounts/' + discount_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_discount_on_lime_item(self, order_id, line_item_id, discount):
        # Define Payload
        payload = discount
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/'
            + line_item_id + '/discounts',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_discount_by_id(self, order_id, line_item_id, discount_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/'
            + line_item_id + '/discounts/' + discount_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Line Items
    def get_line_items_by_order(self, order_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_line_item(self, order_id, line_item):
        # Define Payload
        payload = line_item
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def get_line_item_by_id(self, order_id, line_item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/' + line_item_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def update_line_item_by_id(self, order_id, line_item):
        # Define Payload
        payload = line_item
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/' + line_item["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def void_line_item_by_id(self, order_id, line_item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/' + line_item_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Modifications
    def apply_modification_to_line_item(self, order_id, line_item_id, modification):
        # Define Payload
        payload = modification
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/'
            + line_item_id + '/modifications',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def remove_modification_from_line_item(self, order_id, line_item_id, modification_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/'
            + line_item_id + '/modifications/' + modification_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # BulkLineItems
    def create_bulk_line_items(self, order_id, line_item_request):
        # Define Payload
        payload = line_item_request
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/bulk_line_items',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    # Payments
    def create_payment_record_for_order(self, order_id, payment):
        # Define Payload
        payload = payment
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/payments',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    # Service Charge
    def create_service_charge_for_order(self, order_id, service_charge):
        # Define Payload
        payload = service_charge
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/service_charge',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_service_charge_for_order(self, order_id, charge_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id
            + '/service_charge/' + charge_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # VoidedLineItems

    def void_line_item(self, order_id, voided_line_item):
        # Define Payload
        payload = voided_line_item
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/voided_line_items',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def get_voided_order_line_items(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/voided_line_items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Exchange
    def create_or_exchange_line_item(self, order_id, old_line_item_id, line_item_id, line_item):
        # Define Payload
        payload = line_item
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/orders/' + order_id + '/line_items/'
            + old_line_item_id + '/exchange/' + line_item_id,
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()
