from cloverapi.cloverapi_auth import CloverApiAuth
from cloverapi.services.merchant_service import MerchantService
from cloverapi.services.cash_service import CashService
from cloverapi.services.customer_service import CustomerService
from cloverapi.services.employee_service import EmployeeService
from cloverapi.services.inventory_service import InventoryService
from cloverapi.services.notification_service import NotificationService
from cloverapi.services.order_service import OrderService
from cloverapi.services.payment_service import PaymentService
from cloverapi.services.app_service import AppService


class CloverApiClient(object):
    def __init__(self, api_key, merchant_id, api_url):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = CloverApiAuth(api_key=api_key)
        # Define Services
        self.merchant_service = MerchantService(self.auth, self.url, self.merchant_id)
        self.cash_service = CashService(self.auth, self.url, self.merchant_id)
        self.customer_service = CustomerService(self.auth, self.url, self.merchant_id)
        self.employee_service = EmployeeService(self.auth, self.url, self.merchant_id)
        self.inventory_service = InventoryService(self.auth, self.url, self.merchant_id)
        self.notification_service = NotificationService(self.auth, self.url, self.merchant_id)
        self.order_service = OrderService(self.auth, self.url, self.merchant_id)
        self.payment_service = PaymentService(self.auth, self.url, self.merchant_id)
        self.app_service = AppService(self.auth, self.url, self.merchant_id)
