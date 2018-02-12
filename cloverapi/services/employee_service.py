import requests


class EmployeeService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Employees
    def get_employees(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/employees/', auth=self.auth, timeout=30,
                         params=payload)
        return r.json()

    def create_employee(self, employee):
        # Define Payload
        payload = employee
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/employees/', auth=self.auth,
                          timeout=30, json=payload)
        return r.json()

    def get_employee_by_id(self, employee_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id, auth=self.auth,
                         timeout=30,
                         params=payload)
        return r.json()

    def update_employee_by_id(self, employee):
        # Define Payload
        payload = employee
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee["id"], auth=self.auth,
                          timeout=30,
                          params=payload)
        return r.json()

    def delete_employee_by_id(self, employee_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id,
                            auth=self.auth,
                            timeout=30,
                            params=payload)
        return r.json()

    # Shifts
    def get_shifts(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/shifts/', auth=self.auth,
                         timeout=30,
                         params=payload)
        return r.json()

    def get_shift_by_id(self, shift_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/shifts/' + shift_id, auth=self.auth,
                         timeout=30,
                         params=payload)
        return r.json()

    def get_shifts_by_employee_id(self, employee_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/shifts',
                         auth=self.auth,
                         timeout=30,
                         params=payload)
        return r.json()

    def create_shift_by_employee_id(self, employee_id, shift):
        # Define Payload
        payload = shift
        # Send Request
        r = requests.post(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/shifts',
                          auth=self.auth,
                          timeout=30,
                          json=payload)
        return r.json()

    def get_employee_shift_by_shift_id(self, employee_id, shift_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/shifts/'
                         + shift_id,
                         auth=self.auth,
                         timeout=30,
                         params=payload)
        return r.json()

    def update_employee_shift_by_shift_id(self, employee_id, shift):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/shifts/' + shift["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_employee_shift_by_shift_id(self, employee_id, shift_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/shifts/' + shift_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Shifts CSV
    def get_shifts_csv(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/shifts.csv',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Orders
    def get_orders_by_employee_id(self, employee_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/employees/' + employee_id + '/orders',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # EmployeeCards
    def get_employee_cards(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/employee_cards',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_employee_cards(self, employee_card):
        # Define Payload
        payload = employee_card
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/employee_cards',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def get_employee_card_by_id(self, employee_card_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/employee_cards/' + employee_card_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def delete_employee_card_by_id(self, employee_card_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/employee_cards/' + employee_card_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()
