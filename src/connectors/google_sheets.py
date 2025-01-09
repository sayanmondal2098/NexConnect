from .base_connector import BaseConnector

class GoogleSheetsConnector(BaseConnector):
    def push_data(self, data):
        print(f"Pushing data to Google Sheets: {data}")
