import json
from mikrotik.connection import MikrotikConnection

class MikrotikManager:

    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.routers = {}
        self.connections = {}

        self.load_credentials()

    def load_credentials(self):

        with open(self.credentials_file, "r", encoding="utf-8") as file:
            self.routers = json.load(file)

    def connect_all(self):

        for router_id, config in self.routers.items():

            print(
                f"Conectando a {router_id} "
                f"({config['host']})..."
            )

            connection = MikrotikConnection(
                host=config["host"],
                username=config["username"],
                password=config["password"],
                api_port=config.get("api_port", 8728),
                ssl=config.get("ssl", False)
            )

            api = connection.connect()
            if api:
                self.connections[router_id] = connection
                print(f"[OK] {router_id}")
            else:
                print(f"[ERROR] {router_id}")

    def get_connection(self, router_id):

        return self.connections.get(router_id)