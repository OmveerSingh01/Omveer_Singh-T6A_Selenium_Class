from core.base_api import BaseApi
from utils.config import base_url

class user_register:
    def __init__(self):
        self.api = BaseApi(base_url)

    def register(self,payload):
        return self.api.post('/shoppers',json=payload)