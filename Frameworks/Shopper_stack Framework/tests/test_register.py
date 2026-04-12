# from api.Shopper_Profile.user_register import user_register
from api.Shopper_Profile.user_register import user_register
from utils.read_data import read_json

register_api = user_register()

def test_register():
    data = read_json("test_data/register.json")

    response = register_api.register(data)

    assert response.status_code == 200,response.text
    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)