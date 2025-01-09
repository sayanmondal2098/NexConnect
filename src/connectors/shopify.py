from .base_connector import BaseConnector

class ShopifyConnector(BaseConnector):
    def fetch_data(self):
        return ["Shopify order 1", "Shopify order 2"]
