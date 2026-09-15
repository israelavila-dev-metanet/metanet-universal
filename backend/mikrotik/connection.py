import routeros_api

class MikrotikConnection:
    def __init__(self, host, username,password, ssl=False, api_port=8728):
        self.host = host
        self.username = username
        self.password = password
        self.ssl = ssl
        self.api_port = api_port

    def connect(self):
        api = routeros_api.RouterOsApiPool(
            self.host,
            self.username,
            self.password,
            use_ssl=self.ssl,
            port=self.api_port,
        )
        try:
            return api.get_api()
        except Exception as e:
            print(f"Error al conectar a {self.host}: {e}")
            return None
        
    def get_identity(self):

        api = self.connect()

        if api:

            resource = api.get_resource("/system/identity")

            result = resource.get()

            if result:
                return result[0].get("name")

        return None
    
    def get_version(self):

        api = self.connect()

        if api:

            resource = api.get_resource("/system/resource")

            result = resource.get()

            if result:
                return result[0].get("version")

        return None

    def get_users_pppoe(self):

        api = self.connect()

        if not api:
            return None

        try:
            result = api.get_resource("/ppp/active").get()

            return len(result)

        except Exception as e:

            print(
                f"Error obteniendo PPPoE activos "
                f"de {self.host}: {e}"
            )

            return None
        