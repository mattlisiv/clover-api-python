import requests


class NotificationService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Notifications
    def create_notification_for_app(self, app_id, app_notification):
        # Define Payload
        payload = app_notification
        # Send Request
        r = requests.post(
            self.url + '/v3/apps/' + app_id + '/merchants/' + self.merchant_id + '/notifications/',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def create_notification_for_device(self, app_id, device_id, app_notification):
        # Define Payload
        payload = app_notification
        # Send Request
        r = requests.post(
            self.url + '/v3/apps/' + app_id + '/devices/' + device_id + '/notifications/',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()
