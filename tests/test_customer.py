import pytest
import random
from faker import Faker
from cloverapi.helpers.creator import Creator
from cloverapi.cloverapi_client import CloverApiClient
fake = Faker()
api_client = CloverApiClient(api_key='XXXX', merchant_id='XXXX',
                             api_url='https://apisandbox.dev.clover.com')


def test_create_user():
    customer_since = random.randrange(0, 3000, 1)
    first_name = fake.name()
    last_name = fake.name()
    customer = Creator.create_customer(customer_since=customer_since, first_name=first_name, last_name=last_name)
    assert customer['firstName'] == first_name
    assert customer['lastName'] == last_name
    assert customer['customerSince'] == customer_since





