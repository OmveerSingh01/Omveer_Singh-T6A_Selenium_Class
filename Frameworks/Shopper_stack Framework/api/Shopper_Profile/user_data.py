from wsgiref import headers

from core.base_api import BaseApi
from utils.config import base_url

class user_data():
    def __init__(self):
        self.api = BaseApi(base_url)

    def datta(self,shopperId,headers):
        return  self.api.get( f'/shoppers/{shopperId}',headers=headers)