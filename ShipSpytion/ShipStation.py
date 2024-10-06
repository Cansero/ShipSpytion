import json
from requests import request
from time import sleep
from datetime import datetime

from .Exceptions import NotImplementedError

from .Models import Limits, Tag, Order
from .AdditionalModels import Carrier, Package, Service


ORDER_STATUS = [
        "awaiting_payment",
        "awaiting_shipment",
        "shipped",
        "on_hold",
        "cancelled"
        ]

CONFIRMATION = [
        "none",
        "delivery",
        "signature",
        "adult_signature",
        "direct_signature"
        ]


class ShipStation:
    def __init__(self, token, debug=False):
        self.debug = debug

        self.url = "https://ssapi.shipstation.com"
        self.token = token
        self.timeout = 10  # TODO: Confirm Usage
        self.limits = Limits()

    def _request_handler(self,
                         request_type: str,
                         url: str,
                         data: dict = None) -> dict | str:
        # WARNING: No Toekn handling
        url = self.url + url

        if self.debug:
            print(url)

        headers = {"Authorization": f"Basic {self.token}"}
        if request_type == "post":
            headers["content-type"] = "application/json"

        done = False
        while not done:

            # WARNING: Handle remianing uses before the requests
            data = json.dumps(data)
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

    # NOTE: Not tried
    def add_funds_to_carrier(self, carrier: Carrier, amount: int):
        if not isinstance(carrier, Carrier):
            return
        if not isinstance(amount, int):
            return

        url = "/carriers/addfunds"
        data = {"carrierCode": carrier.code, "amount": amount}
        response = self._request_handler("post", url, data)

        carrier.update(response)

        return

    def get_carrier_info(self, code: str) -> Carrier:
        url = f"/carriers/getcarrier?carrierCode={code}"
        carrier = self._request_handler("get", url)

        c = Carrier()
        c.update(carrier)

        return c

    def list_carriers(self) -> list[Carrier]:
        url = "/carriers"
        carriers = self._request_handler("get", url)

        r_carriers = []
        for carrier in carriers:
            c = Carrier()
            c.update(carrier)
            r_carriers.append(c)

        return r_carriers

    def list_packages(self, carrier: Carrier) -> list[Package]:
        if not isinstance(carrier, Carrier):
            return

        url = f"/carriers/listpackages?carrierCode={carrier.code}"
        packages = self._request_handler("get", url)

        r_packages = []
        for package in packages:
            p = Package()
            p.update(package)
            r_packages.apend(p)

        return r_packages

    def list_services(self, carrier: Carrier) -> list[Service]:
        if not isinstance(carrier, Carrier):
            return

        url = f"/carriers/listservices?carrierCode={carrier.code}"
        services = self._request_handler("get", url)

        r_services = []
        for service in services:
            s = Service()
            s.update(service)
            r_services.append(s)

        return r_services

    # FIX: Poorly implemented
    def get_customer_info(self, customerId):
        url = f"/customers/{customerId}"
        customer = self._request_handler("get", url)

        return customer

    # FIX: Not implemented
    def list_customers(self):
        raise NotImplementedError("list_customers not implemented yet")

    def list_fulfillments(self):
        raise NotImplementedError("list_fulfillments not implemented yet")

    def list_account_tags(self) -> list[Tag]:
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

    def assign_user(self, orders, user):
        # WARNING: Add User Class for this function
        pass

    def create_label_for_order(
            self,
            order: Order,
            carrier: Carrier,
            service: Service,
            confirmation,
            shipDate="",
            testLabel=False
            ):
        if not isinstance(order, Order):
            return
        if not isinstance(carrier, Carrier):
            return
        if not isinstance(service, Service):
            return
        if confirmation not in CONFIRMATION:
            return

        shipDate = datetime.today().strftime('%Y-%m-%d') if shipDate == "" else shipDate
        data = {
                "orderId": order.orderId,
                "carrierCode": carrier.code,
                "serviceCode": service.code,
                "confirmation": confirmation,
                "shipDate": shipDate,
                "weight": order.weight.as_dict(),
                "dimensions": order.dimensions.as_dict(),
                "insuranceOptions": order.insuranceOptions.as_dict(),
                "internationalOptions": "",
                "advancedOptions": "",
                "testLabel": testLabel
                }

    # NOTE: Could be optimized
    def get_all_orders(self) -> list[Order]:
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

    def list_by_tags(self, orderStatus, tag: Tag, page=1, pageSize=1):
        if orderStatus not in ORDER_STATUS:
            return
        if not isinstance(tag, Tag):
            return

        url = f"/listbytag?orderStatus={orderStatus}&tagId={tag.tagId}&page={page}&pageSize={pageSize}"
        content = self._request_handler("get", url)

        return content["orders"]

    def _get_n_order(self, amount) -> list[Order]:
        if amount < 1 or amount > 500:
            return
        url = f"/orders?pageSize={amount}"
        content = self._request_handler("get", url)
        orders = []
        for order in content["orders"]:
            self._add_order(order, orders)
        return orders

    def add_tag(self, order: Order, tag: Tag) -> bool:
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
