from ShipStation import ShipStation
from Token import token

ss = ShipStation(token=token, debug=False)
order = ss._get_n_order(1)[0]

print(order.as_dict())
print(type(order.billTo))
