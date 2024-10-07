from .BaseModel import BaseModel


class Carrier(BaseModel):
    '''
    Examples shown in https://www.shipstation.com/docs/api/carriers/list/
    describe accountNumber as either string or integer
    '''

    def __init__(
            self,
            name="",
            code="",
            accountNumber=None,
            requiresFundedAccount=True,
            balance=0,
            nickname="",
            shippingProviderId=0,
            primary=False
            ):
        self.name = name
        self.code = code
        self.accountNumber = accountNumber
        self.requiresFundedAccount = requiresFundedAccount
        self.balance = balance
        self.nickname = nickname
        self.shippingProviderId = shippingProviderId
        self.primary = primary


class Package(BaseModel):
    def __init__(
            self,
            carrierCode="",
            code="",
            name="",
            domestic=False,
            international=False
            ):
        self.carrierCode = carrierCode
        self.code = code
        self.name = name
        self.domestic = domestic
        self.international = international


# FIX: This two (up and down) share same code


class Service(BaseModel):
    def __init__(
            self,
            carrierCode="",
            code="",
            name="",
            domestic=False,
            international=False
            ):
        self.carrierCode = carrierCode
        self.code = code
        self.name = name
        self.domestic = domestic
        self.international = international


class Shipment(BaseModel):
    def __init__(
            self,
            shipmentId=0,
            shipmentCost=0,
            insuranceCost=0,
            trackingNumber="",
            labelData="",
            formData=None
            ):
        self.shipmentId = shipmentId
        self.shipmentCost = shipmentCost
        self.insuranceCost = insuranceCost
        self.trackingNumber = trackingNumber
        self.labelData = labelData
        self.formData = formData


class ListOrdersOptions(BaseModel):
    def __init__(
            self,
            customerName="",
            itemKeyword="",
            createDateStart="",
            createDateEnd="",
            customerCountryCode="",
            modifyDateStart="",
            modifyDateEnd="",
            orderDateStart="",
            orderDateEnd="",
            orderNumber="",
            orderStatus="",
            paymentDateStart="",
            paymentDateEnd="",
            storeId=0,
            sortBy="",
            sortDir="",
            page="",
            pageSize=""
            ):
        self.customerName = customerName
        self.itemKeyword = itemKeyword
        self.createDateStart = createDateStart
        self.createDateEnd = createDateEnd
        self.customerCountryCode = customerCountryCode
        self.modifyDateStart = modifyDateStart
        self.modifyDateEnd = modifyDateEnd
        self.orderDateStart = orderDateStart
        self.orderDateEnd = orderDateEnd
        self.orderNumber = orderNumber
        self.orderStatus = orderStatus
        self.paymentDateStart = paymentDateStart
        self.paymentDateEnd = paymentDateEnd
        self.storeId = storeId
        self.sortBy = sortBy
        self.sortDir = sortDir
        self.page = page if page else "1"
        self.pageSize = pageSize if 0 < pageSize < 501 else 1
