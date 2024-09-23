import json
from requests import request
from time import sleep

from Models import Limits, Tag, Order


class ShipStation:
    def __init__(self, token=None):
        self.url = "https://ssapi.shipstation.com"
        self.token = token
        self.timeout = 10  # TODO: Confirm Usage
        self.limits = Limits()

    def _request_handler(self, request_type, url, data=None):
        url = self.url + url

        headers = {"Authorization": f"Basic {self.token}"}
        if request_type == "post":
            headers["content-type"] = "application/json"

        done = False
        while not done:

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

        return json.loads(r.text)

    def list_tags(self):
        url = "/accounts/listtags"
        tags = self._request_handler("get", url)

        r_tags = []
        if tags:
            for tag in tags:
                t = Tag()
                t.update(tag)
                r_tags.apped(t)

        return r_tags

    def get_orders(self):
        url = "/orders?pageSize=500"
        content = self._request_handler("get", url)

        for order in content["orders"]:
            pass
