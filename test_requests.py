from ShipStation import ShipStation
from Token import token

ss = ShipStation(token=token)
url = "/orders?pageSize=1"
response = ss._request_handler("get", url)
print("Headers -------------------------------------------")
print(response.headers)
print("Body ----------------------------------------------")
print(response.text)
