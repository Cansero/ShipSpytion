class Tag:
    def __init__(self, tagid=None, name=None, color=None):
        self.tagid = tagid
        self.name = name
        self.color = color

    def update(self, ref):
        if not isinstance(ref, dict):
            return

        self.tagid = ref['tagId']
        self.name = ref['name']
        self.color = ref['color']


class Limits:
    def __init__(self, limit_limit=10, limit_reset=60, limit_remaining=10):
        self.limit_limit = limit_limit
        self.limit_reset = limit_reset
        self.limit_remaining = limit_remaining

    def update(self, ref):
        if not isinstance(ref, dict):
            return

        self.limit_limit = ref['X-Rate-Limit-Limit']
        self.limit_reset = ref['X-Rate-Limit-Reset']
        self.limit_remaining = ref['X-Rate-Limit-Remaining']


class Order:
    def __init__(self,
                 ref,
                 orderId="",
                 orderNumber="",
                 orderKey="",
                 orderDate="",
                 createDate="",
                 modifyDate="",
                 paymentDate="",
                 shipByDate="",
                 orderStatus="",
                 customerId="",
                 customerUsername="",
                 customerEmail="",
                 billTo="",
                 shipTo="",
                 items="",
                 orderTotal="",
                 amountPaid="",
                 taxAmount="",
                 shippingAmount="",
                 customerNotes="",
                 internalNotes="",
                 gift="",
                 giftMessage="",
                 paymentMethod="",
                 requestedShippingService="",
                 carrierCode="",
                 serviceCode="",
                 packageCode="",
                 confirmation="",
                 shipDate="",
                 holdUntilDate="",
                 weight="",
                 dimensions="",
                 insuranceOptions="",
                 advancedOptions="",
                 tagIds="",
                 userId="",
                 externallyFulfilled="",
                 externallyFulfilledBy=""
                 ):
        self.orderId = orderId
        self.orderNumber = orderNumber
        self.orderKey = orderKey
        self.orderDate = orderDate
        self.createDate = createDate
        self.modifyDate = modifyDate
        self.paymentDate = paymentDate
        self.shipByDate = shipByDate
        self.orderStatus = orderStatus
        self.customerId = customerId
        self.customerUsername = customerUsername
        self.customerEmail = customerEmail
        self.billTo = billTo
        self.shipTo = shipTo
        self.items = items
        self.orderTotal = orderTotal
        self.amountPaid = amountPaid
        self.taxAmount = taxAmount
        self.shippingAmount = shippingAmount
        self.customerNotes = customerNotes
        self.internalNotes = internalNotes
        self.gift = gift
        self.giftMessage = giftMessage
        self.paymentMethod = paymentMethod
        self.requestedShippingService = requestedShippingService
        self.carrierCode = carrierCode
        self.serviceCode = serviceCode
        self.packageCode = packageCode
        self.confirmation = confirmation
        self.shipDate = shipDate
        self.holdUntilDate = holdUntilDate
        self.weight = weight
        self.dimensions = dimensions
        self.insuranceOptions = insuranceOptions
        self.advancedOptions = advancedOptions
        self.tagIds = tagIds
        self.userId = userId
        self.externallyFulfilled = externallyFulfilled
        self.externallyFulfilledBy = externallyFulfilledBy

        if ref:
            keys = vars(self).keys()
            for k, v in ref.items():
                if k in keys:
                    setattr(self, k, v)
