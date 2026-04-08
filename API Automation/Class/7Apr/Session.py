import requests
import urllib3
from redis.commands import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = 'https://www.shoppersstack.com/shopping'
session = requests.Session()


'''payload = {
  "city": "parbatsar",
  "country": "India",
  "email": "Raj010@gmail.com",
  "firstName": "Raj",
  "gender": "MALE",
  "lastName": "Singh",
  "password": "Raj1234",
  "phone": 9888739289,
  "state": "Rajasthan",
  "zoneId": "ALPHA"
}

def posting():
    response = requests.post('https://www.shoppersstack.com/shopping/shoppers', json=payload, verify=False)
    print(response.status_code)
    print(response.text)
    print(response.json())

# posting()
print()
'''
# ------LOGIN PAYLOAD ------
payload2 = {
  "email": "Raj010@gmail.com",
  "password": "Raj1234",
  "role": "SHOPPER"
}

data = None
def post_login():
    res2 = session.post('https://www.shoppersstack.com/shopping/users/login', json=payload2, verify=False)
    assert res2.status_code == 200, "Login Failed"
    data = res2.json()
    return data

datta = post_login()
userid = datta['data']['userId']
token = datta['data']['jwtToken']
print(f'User id : {userid}')
print(f'Token : {token}')

header = {
    "Authorization" : f"Bearer {token}"
}


def get_userid():
    res3 = session.get(f'https://www.shoppersstack.com/shopping/shoppers/{userid}', headers=header, verify=False)
    print(res3.status_code)

# posting()
post_login()
get_userid()