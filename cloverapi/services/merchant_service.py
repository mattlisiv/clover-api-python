import requests


class MerchantService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Merchants
    def get_merchant(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id, auth=self.auth, timeout=30, params=payload)
        return r.json()

    def update_merchant(self, merchant):
        # Define Payload
        payload = merchant
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id, auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Address
    def get_merchant_address(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/address', auth=self.auth, timeout=30,
                         params=payload)
        return r.json()

    # Gateway
    def get_gateway(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/gateway', auth=self.auth, timeout=30,
                         params=payload)
        return r.json()

    # Properties
    def get_properties(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/properties', auth=self.auth, timeout=30,
                         params=payload)
        return r.json()

    def update_properties(self, properties):
        # Define Payload
        payload = properties
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/properties', auth=self.auth, timeout=30,
                          json=payload)
        return r.json()

    # Default Service Charge
    def get_default_service_charge(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/default_service_charge', auth=self.auth,
                         timeout=30, params=payload)
        return r.json()

    # Tip Suggestions
    def get_tip_suggestion(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/tip_suggestions', auth=self.auth, timeout=30,
                         params=payload)
        return r.json()

    def update_tip_suggestion_by_id(self, tip_suggestion):
        # Define Payload
        payload = tip_suggestion
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/tip_suggestions/' + tip_suggestion["id"], auth=self.auth,
                          timeout=30, json=payload)
        return r.json()

    def get_tip_suggestion_by_id(self, tip_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/tip_suggestions/' + tip_id, auth=self.auth,
                         timeout=30, params=payload)
        return r.json()

    # Order Types
    def get_order_types(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/order_types/', auth=self.auth,
                         timeout=30, params=payload)
        return r.json()

    def create_order_types(self, order_type):
        # Define Payload
        payload = order_type
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/order_types/', auth=self.auth, timeout=30,
                          json=payload)
        return r.json()

    def get_order_type_by_id(self, order_type_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/order_types/' + order_type_id,
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def update_order_type_by_id(self, order_type):
        # Define Payload
        payload = order_type
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/order_types/' + order_type["id"],
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_order_type_by_id(self, order_type_id):
        # Define Payload
        payload = {}
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/order_types/' + order_type_id,
                            auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Order Type Categories
    def create_or_delete_order_type_category(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/order_type_categories/',
                          auth=self.auth, timeout=30, params=payload)
        return r.json()

    # System Order Types
    def get_system_order_types(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/system_order_types/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Roles
    def get_roles(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/roles/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def create_role(self, role):
        # Define Payload
        payload = role
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/roles/',
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def get_role_by_id(self, role_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/roles/' + role_id,
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def update_role_by_id(self, role):
        # Define Payload
        payload = role
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/roles/' + role["id"],
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_role_by_id(self, role_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/roles/' + role_id,
                            auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Tenders
    def get_tenders(self, filter=None):
        # Define Payload
        payload = {}
        if filter is not None:
            payload['filter'] = filter
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/tenders/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def add_tender(self, tender):
        # Define Payload
        payload = tender
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/tenders/',
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def get_tender_by_id(self, tender_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/tenders/' + tender_id,
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def update_tender_by_id(self, tender):
        # Define Payload
        payload = tender
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/tenders/' + tender["id"],
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_tender_by_id(self, tender_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/tenders/' + tender_id,
                            auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Opening Hours
    def get_opening_hours(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/opening_hours/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def create_opening_hours(self, opening_hour):
        # Define Payload
        payload = opening_hour
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/opening_hours/',
                          auth=self.auth, timeout=30, json=opening_hour)
        return r.json()

    def get_opening_hours_by_id(self, opening_hours_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/opening_hours/' + opening_hours_id,
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def update_opening_hours_by_id(self, opening_hour):
        # Define Payload
        payload = opening_hour
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/opening_hours/' + opening_hour["id"],
                          auth=self.auth, timeout=30, json=payload)
        return r.json()

    def delete_opening_hours_by_id(self, opening_hours_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/opening_hours/' + opening_hours_id,
                            auth=self.auth, timeout=30, params=payload)
        return r.json()

    # Devices
    def get_merchant_devices(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/devices/',
                         auth=self.auth, timeout=30, params=payload)
        return r.json()

    def get_merchant_device_by_id(self, device_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/devices/' + device_id,
                         auth=self.auth, timeout=30, params=payload)
        return r.json()
