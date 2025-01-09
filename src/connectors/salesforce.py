from .base_connector import BaseConnector

class SalesforceConnector(BaseConnector):
    def fetch_data(self):
        return ["Salesforce record 1", "Salesforce record 2"]
