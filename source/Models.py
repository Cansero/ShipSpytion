from BaseModel import BaseModel
from SubModels import (
        Address,
        AdvancedOptions,
        Dimensions,
        InsuranceOptions,
        InternationalOptions,
        OrderItem,
        ProductCategory,
        ProductTag,
        ProductType,
        Weight
        )


class Limits:
    def __init__(
            self,
            limit_limit=10,
            limit_reset=60,
            limit_remaining=10
            ):
        self.limit_limit = limit_limit
        self.limit_reset = limit_reset
        self.limit_remaining = limit_remaining

    def update(self, ref):
        if not isinstance(ref, dict):
            return

        self.limit_limit = ref['X-Rate-Limit-Limit']
        self.limit_reset = ref['X-Rate-Limit-Reset']
        self.limit_remaining = ref['X-Rate-Limit-Remaining']


class Tag(BaseModel):
    def __init(self,
               tagId="",
               name="",
               color=""
               ):
        self.tagId = tagId
        self.name = name
        self.color = color


class Order(BaseModel):
    def __init__(
            self,
            orderId=0,
            orderNumber="",
            orderKey="",
            orderDate="",
            createDate="",
            modifyDate="",
            paymentDate="",
            shipByDate="",
            orderStatus="",
            customerId=0,
            customerUsername="",
            customerEmail="",
            billTo=Address(),
            shipTo=Address(),
            items=None,  # List if OrderItem
            orderTotal=0,
            amountPaid=0,
            taxAmount=0,
            shippingAmount=0,
            customerNotes="",
            internalNotes="",
            gift=False,
            giftMessage="",
            paymentMethod="",
            requestedShippingService="",
            carrierCode="",
            serviceCode="",
            packageCode="",
            confirmation="",
            shipDate="",
            holdUntilDate="",
            weight=Weight(),
            dimensions=Dimensions(),
            insuranceOptions=InsuranceOptions(),
            internationalOptions=InternationalOptions(),
            advancedOptions=AdvancedOptions(),
            tagIds=None,
            userId="",
            externallyFulfilled=False,
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
        self.items = [OrderItem()] if items is None else items
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
        self.internationalOptions = internationalOptions
        self.advancedOptions = advancedOptions
        self.tagIds = tagIds
        self.userId = userId
        self.externallyFulfilled = externallyFulfilled
        self.externallyFulfilledBy = externallyFulfilledBy


class Product(BaseModel):
    def __init__(
            self,
            productId=0,
            sku="",
            name="",
            price=0,
            defaultCost=0,
            length=0,
            width=0,
            height=0,
            weightOz=0,
            internalNotes="",
            fulfillmentSku="",
            createDate="",
            modifyDate="",
            active=False,
            productCategory=ProductCategory(),
            productType=ProductType(),
            warehouseLocation="",
            defaultCarrierCode="",
            defaultServiceCode="",
            defaultPackageCode="",
            defaultIntlCarrierCode="",
            defaultIntlServiceCode="",
            defaultIntlPackageCode="",
            defaultConfirmation="",
            defaultIntlConfirmation="",
            customsDescription="",
            customsValue=0,
            customsTariffNo="",
            customsCountryCode="",
            noCustoms=False,
            tags=ProductTag()
            ):
        self.productId = productId
        self.sku = sku
        self.name = name
        self.price = price
        self.defaultCost = defaultCost
        self.length = length
        self.width = width
        self.height = height
        self.weightOz = weightOz
        self.internalNotes = internalNotes
        self.fulfillmentSku = fulfillmentSku
        self.createDate = createDate
        self.modifyDate = modifyDate
        self.active = active
        self.productCategory = productCategory
        self.productType = productType
        self.warehouseLocation = warehouseLocation
        self.defaultCarrierCode = defaultCarrierCode
        self.defaultServiceCode = defaultServiceCode
        self.defaultPackageCode = defaultPackageCode
        self.defaultIntlCarrierCode = defaultIntlCarrierCode
        self.defaultIntlServiceCode = defaultIntlServiceCode
        self.defaultIntlPackageCode = defaultIntlPackageCode
        self.defaultConfirmation = defaultConfirmation
        self.defaultIntlConfirmation = defaultIntlConfirmation
        self.customsDescription = customsDescription
        self.customsValue = customsValue
        self.customsTariffNo = customsTariffNo
        self.customsCountryCode = customsDescription
        self.noCustoms = noCustoms
        self.tags = tags


# FIX: Class Webhook Omitted
