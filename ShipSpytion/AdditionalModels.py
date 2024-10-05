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
