
import requests


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}/{endpoint.lstrip('/')}") 

    def post(self, endpoint, data):
        return self.session.post(f"{self.base_url}/{endpoint.lstrip('/')}", json=data)


    def put(self, endpoint, data):
        return self.session.put(f"{self.base_url}/{endpoint.lstrip('/')}", json=data)

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}/{endpoint.lstrip('/')}")