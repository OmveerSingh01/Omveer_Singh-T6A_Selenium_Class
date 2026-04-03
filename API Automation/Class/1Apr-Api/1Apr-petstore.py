import requests


# response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus?status=sold')


#
# print(response.json()['invalid-status-value'])
#
# expected = 2100
# actual = response.status_code
# assert actual == expected,f' Status code Mismatch {actual}'
# print(response.json())


payload = {
  "id": 106,
  "category": {
    "id": 1,
    "name": "panther"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

currID = 0

# POST METHOD
def Posting():
    Presponse = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
    # print(Presponse.json())
    # print(Presponse.status_code)
    # print(Presponse.text)
    global currID
    currID = Presponse.json()['id']
    return currID



# Presponse = requests.post('https://petstore.swagger.io/v2/pet', json=payload)


# Presponse = requests.post('https://petstore.swagger.io/v2/pet', json=payload)
# print(Presponse.json())
# print(Presponse.text)
# print(Presponse.status_code)

# GET METHOD
def getting():
    response = requests.get(f'https://petstore.swagger.io/v2/pet/{currID}')
    # print(response.text)
    print(response.status_code)
    print(response.json())
    # return response.json()['id']




# DELETE METHOD
def Deleting():
    Dresponse = requests.delete(f'https://petstore.swagger.io/v2/pet/{currID}')
    print(Dresponse.status_code)
    print(Dresponse.json())
    # return Dresponse.json()['id']

print(Posting())
getting()
Deleting()
# print(Dresponse.text)
