import json
from requests import request
from time import sleep

from Models import Limits, Tag, Order


class ShipStation:
    def __init__(self, token=None, debug=False):
        self.debug = debug

        self.url = "https://ssapi.shipstation.com"
        self.token = token
        self.timeout = 10  # TODO: Confirm Usage
        self.limits = Limits()

    def _request_handler(self,
                         request_type: str,
                         url: str,
                         data: dict = None) -> dict | str:
        url = self.url + url

        if self.debug:
            print(url)

        headers = {"Authorization": f"Basic {self.token}"}
        if request_type == "post":
            headers["content-type"] = "application/json"

        done = False
        while not done:

            # WARNING: Handle remianing uses before the requests

            r = request(request_type, url, headers=headers, data=data)

            self.limits.update(r.headers)

            match r.status_code:
                case 200 | 201 | 204:
                    done = True
                case 400 | 401 | 403 | 404 | 405:
                    print("http error")
                    print(r.text)
                    done = True
                case 429:  # Too many requests
                    print("Too many requests")
                    sleep(self.limits.limit_reset)
                case 500:
                    print("http 500")  # Don't actually remember what that means lol
                    sleep(5)
        if self.debug:
            print("Headers -------------------------------------------")
            print(r.headers)
            print("Body ----------------------------------------------")
            print(r.text)

        if r.text:
            return json.loads(r.text)
        else:
            return "No body"

    def list_tags(self) -> list[Tag]:
        url = "/accounts/listtags"
        tags = self._request_handler("get", url)

        r_tags = []
        if tags:
            for tag in tags:
                if self.debug:
                    print(tag)

                t = Tag()
                t.update(tag)
                r_tags.append(t)

        return r_tags

    # NOTE: Could be optimized
    def get_orders(self) -> list[Order]:
        url = "/orders?pageSize=500"
        content = self._request_handler("get", url)

        orders = []
        for order in content["orders"]:
            self._add_order(order, orders)

        pages = int(content["pages"])
        if pages > 1:
            for i in range(2, pages + 1):
                n_url = url
                n_url += f"&page={i}"
                content = self._request_handler("get", n_url)

                for order in content["orders"]:
                    self._add_order(order, orders)

        return orders

    def _get_n_order(self, amount) -> list[Order]:
        if amount < 1 or amount > 500:
            return
        url = f"/orders?pageSize={amount}"
        content = self._request_handler("get", url)
        orders = []
        for order in content["orders"]:
            self._add_order(order, orders)
        return orders

    def add_tag(self, order: Order, tag: Tag) -> dict:
        if not isinstance(order, Order) and not isinstance(tag, Tag):
            return

        url = "/orders/addtag"
        data = {"orderId": order.orderId, "tagId": tag.tagId}
        response = self._request_handler("post", url, data=data)

        return response["success"]

    def _add_order(self, order: dict, list_orders: list):
        o = Order()
        o.update(order)
        list_orders.append(o)
