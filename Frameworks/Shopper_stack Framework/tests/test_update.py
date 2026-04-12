from api.Shopper_Profile.update_shopper import update_shopper
from utils.read_data import read_json
from core.auth import get_auth_data

register_api = update_shopper()

def test_updated():
    data = read_json("test_data/update_shopper.json")
    sId = get_auth_data()
    shopper_id = sId["shopper_id"]
    # shopper_id = 383645
    response = register_api.update(shopper_id,data)
    print(response.status_code)
    print(response.text)
    assert response.status_code == 200,response.text
    res_json = response.json()
    shopper_id = res_json["data"]["userId"]
    print("SHOPPER ID:", shopper_id)