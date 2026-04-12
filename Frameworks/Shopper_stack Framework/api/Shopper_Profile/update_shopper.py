from core.base_api import BaseApi
from utils.config import base_url

class update_shopper():
    def __init__(self):
        self.api = BaseApi(base_url)

    def update(self,shopper_id,payload):
        return self.api.patch(f'/shoppers/{shopper_id}', json=payload)