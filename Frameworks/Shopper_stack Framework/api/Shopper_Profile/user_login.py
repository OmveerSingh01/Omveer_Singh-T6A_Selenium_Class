from core.base_api import BaseApi
from utils.config import base_url

class user_login:
    def __init__(self):
        self.api = BaseApi(base_url)

    def login(self,payload):
        return self.api.post('/users/login',json=payload)