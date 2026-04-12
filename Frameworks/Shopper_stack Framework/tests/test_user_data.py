# from api.Shopper_Profile.user_register import user_register
from api.Shopper_Profile.user_data import user_data
from utils.read_data import read_json

register_api = user_data()

def test_user_data():
    data = read_json("test_data/register.json")

    response = register_api.datta(shopperId=data["data"]["shopperId"],headers=data["data"]["headers"])
    assert response.status_code == 200
    res_json = response.json()

    # assert response.status_code == 200,response.text
    # res_json = response.json()
    # shopper_id = res_json["data"]["userId"]
    # print("SHOPPER ID:", shopper_id)