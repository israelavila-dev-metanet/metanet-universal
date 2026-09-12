import routeros_api
import json

class MikrotikConnection:
    def __init__(self,host,username, password,api_port=8728,ssl=False):
        self.host = host
        self.username = username
        self.password = password
        self.api_port = api_port
        self.ssl = ssl
        self.connection = None
        self.api = None

    def connect(self):
        try:
            self.connect=rouiteros_api.RouterOsApiPöol(self.host, self.username, self.password, port=self.api_port, ssl=self.ssl)
            self.api = self.connect.get_api()
        except Exception as e:
            print(f"Error connecting to Mikrotik router: {e}")
            raise
