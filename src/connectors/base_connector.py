class BaseConnector:
    def fetch_data(self):
        raise NotImplementedError

    def push_data(self, data):
        raise NotImplementedError
