import requests


class InventoryService(object):
    def __init__(self, api_authorization, api_url, merchant_id):
        self.url = api_url.rstrip('/')
        self.merchant_id = merchant_id
        self.auth = api_authorization

    # Inventory

    # Items
    def get_inventory_items(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_inventory_item(self, item):
        # Define Payload
        payload = item
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/items',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def bulk_delete_inventory_items(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_inventory_item_by_id(self, inventory_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/items/' + inventory_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def update_inventory_item_by_id(self, inventory_item):
        # Define Payload
        payload = inventory_item
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/items/' + inventory_item["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def patch_inventory_item_by_id(self, inventory_item):
        # Define Payload
        payload = inventory_item
        # Send Request
        r = requests.patch(
            self.url + '/v3/merchants/' + self.merchant_id + '/items/' + inventory_item["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_inventory_item_by_id(self, inventory_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/items/' + inventory_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_items_by_tag_id(self, tag_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tags/' + tag_id + '/items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_items_by_category_id(self, category_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/categories/' + category_id + '/items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_items_by_tax_rate(self, tax_rate_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rates/' + tax_rate_id + '/items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Item Stocks
    def get_item_stocks(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_stocks',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_item_stock_by_id(self, item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_stocks/' + item_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def update_item_stock_by_id(self, item_id, item_stock):
        # Define Payload
        payload = item_stock
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_stocks/' + item_id,
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_item_stock_by_id(self, item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_stocks/' + item_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Item Groups
    def get_item_groups(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_groups',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_item_group_by_id(self, item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_groups/' + item_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_item_group(self, item_group):
        # Define Payload
        payload = item_group
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_groups',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_item_group_by_id(self, item_group):
        # Define Payload
        payload = item_group
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_groups/' + item_group["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_item_group_by_id(self, item_group_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_groups/' + item_group_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Tags
    def get_tags(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tags',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_tag_by_id(self, tag_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tags/' + tag_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_tag(self, tag):
        # Define Payload
        payload = tag
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/tags',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_tag_by_id(self, tag):
        # Define Payload
        payload = tag
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/tags/' + tag["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_tag_by_id(self, tag_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/tags/' + tag_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_tags_for_item(self, item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/items/' + item_id + '/tags',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Tag Items
    def create_or_delete_tag_items(self, tag_item):
        # Define Payload
        payload = tag_item
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tag_items/',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    # Tax Rates
    def get_tax_rates(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rates',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_tax_rate_by_id(self, tax_rate_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rates/' + tax_rate_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_tax_rate(self, tax_rate):
        # Define Payload
        payload = tax_rate
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rates',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_tax_rate_by_id(self, tax_rate):
        # Define Payload
        payload = tax_rate
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rates/' + tax_rate["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_tax_rate_by_id(self, tax_rate_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rates/' + tax_rate_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Categories
    def get_categories(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/categories',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_category_by_id(self, category_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/categories/' + category_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_category(self, category):
        # Define Payload
        payload = category
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/categories',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_category_by_id(self, category):
        # Define Payload
        payload = category
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/categories/' + category["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_category_by_id(self, category_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/categories/' + category_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_categories_by_item(self, item_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/items/' + item_id + '/categories',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_or_delete_item_category(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/category_items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_or_delete_tax_rate_item(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/tax_rate_items',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Modifier Groups
    def get_modifier_groups(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_modifier_group_by_id(self, modifier_group_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_modifier_group(self, modifier_group):
        # Define Payload
        payload = modifier_group
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_modifier_group_by_id(self, modifier_group):
        # Define Payload
        payload = modifier_group
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_modifier_group_by_id(self, modifier_group_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # ItemModifierGroups
    def create_item_modifier_group_association(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/item_modifier_groups',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # ModifierGroupSortOrders
    def update_modifier_group_sort_orders(self, modifier_group_array):
        # Define Payload
        payload = modifier_group_array
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_group_sort_orders',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    # Modifiers
    def get_modifiers(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifiers',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_modifier_by_modifier_id(self, modifier_group_id, modifier_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id + '/modifiers/'
            + modifier_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_modifiers_by_modifier_group_id(self, modifier_group_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id + '/modifiers',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_modifier(self, modifier_group_id, modifier):
        # Define Payload
        payload = modifier
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id + '/modifiers',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_modifier(self, modifier_group_id, modifier):
        # Define Payload
        payload = modifier
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id + '/modifiers/'
            + modifier["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_modifier(self, modifier_group_id, modifier_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/modifier_groups/' + modifier_group_id
            + '/modifiers/' + modifier_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Attributes
    def get_attributes(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_attribute_by_id(self, attribute_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_attribute(self, attribute):
        # Define Payload
        payload = attribute
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_attribute_by_id(self, attribute):
        # Define Payload
        payload = attribute
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_attribute_by_id(self, attribute_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    # Options
    def get_options(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/options',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_options_by_attribute_id(self, attribute_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id + '/options/',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def get_option_by_option_id(self, attribute_id, option_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.get(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id + '/options/' + option_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_option(self, attribute_id, option):
        # Define Payload
        payload = option
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id + '/options',
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def update_option_by_id(self, attribute_id, option):
        # Define Payload
        payload = option
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id + '/options/' + option["id"],
            auth=self.auth,
            timeout=30,
            json=payload)
        return r.json()

    def delete_option_by_id(self, attribute_id, option_id):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.delete(
            self.url + '/v3/merchants/' + self.merchant_id + '/attributes/' + attribute_id + '/options/' + option_id,
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()

    def create_or_delete_item_option_association(self):
        # Define Payload
        payload = {}
        # Send Request
        r = requests.post(
            self.url + '/v3/merchants/' + self.merchant_id + '/option_items/',
            auth=self.auth,
            timeout=30,
            params=payload)
        return r.json()
