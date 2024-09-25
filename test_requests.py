from ShipStation import ShipStation
from Token import token

ss = ShipStation(token=token, debug=False)
tags = ss.list_tags()

for tag in tags:
    if tag.name == "SHIPPED ORDER":
        break

orders = ss._get_n_order(2)

for order in orders:
    print(order.orderNumber)
    print(order.shipByDate)
