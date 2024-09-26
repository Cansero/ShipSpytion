class BaseModel:
    def update(self, ref):
        if not isinstance(ref, dict):
            return

        keys = vars(self).keys()
        for k, v in ref.items():
            if k in keys:
                setattr(self, k, v)

    def as_dict(self):
        return vars(self)


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
            billTo="",
            shipTo="",
            items="",
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
            weight="",
            dimensions="",
            insuranceOptions="",
            advancedOptions="",
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


class Address(BaseModel):
    def __init__(
            self,
            name="",
            company="",
            street1="",
            street2="",
            street3="",
            city="",
            state="",
            postalCode="",
            country="",
            phone="",
            residential=False,
            addressVerified=""
            ):
        self.name = name
        self.company = company
        self.street1 = street1
        self.street2 = street2
        self.street3 = street3
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country
        self.phone = phone
        self.residential = residential
        self.addressVerified = addressVerified


class AdvancedOptions(BaseModel):
    def __init__(
            self,
            warehouseId=0,
            nonMachinable=False,
            saturdayDelivery=False,
            containsAlcohol=False,
            storeId=0,
            customField1="",
            customField2="",
            customField3="",
            source="",
            mergedOrSplit=False,
            mergedIds=None,
            parentId=0,
            billToParty="",
            billToAccount="",
            billToPostalCode="",
            billToCountryCode="",
            billToMyOtherAccount=""
            ):
        self.warehouseId = warehouseId
        self.nonMachinable = nonMachinable
        self.saturdayDelivery = saturdayDelivery
        self.containsAlcohol = containsAlcohol
        self.storeId = storeId
        self.customField1 = customField1
        self.customField2 = customField2
        self.customField3 = customField3
        self.source = source
        self.mergedOrSplit = mergedOrSplit
        self.mergedIds = mergedIds
        self.parentId = parentId
        self.billToParty = billToParty
        self.billToAccount = billToAccount
        self.billToPostalCode = billToPostalCode
        self.billToCountryCode = billToCountryCode
        self.billToMyOtherAccount = billToMyOtherAccount


class CustomsItems(BaseModel):
    def __init__(
            self,
            customsItemId="",
            description="",
            quantity=0,
            value=0,
            harmonizedTariffCode="",
            countryOfOrigin=""
            ):
        self.customsItemId = customsItemId
        self.description = description
        self.quantity = quantity
        self.value = value
        self.harmonizedTariffCode = harmonizedTariffCode
        self.countryOfOrigin = countryOfOrigin


class Dimensions(BaseModel):
    def __init__(
            self,
            length=0,
            width=0,
            height=0,
            units=""
            ):
        self.length = length
        self.width = width
        self.height = height
        self.units = units


class InsuranceOptions(BaseModel):
    def __init__(
            self,
            provider="",
            insureShipment=False,
            insuredValue=0
            ):
        self.provider = provider
        self.insureShipment = insureShipment
        self.insuredValue = insuredValue


class InternationalOptions(BaseModel):
    def __init__(
            self,
            contents="",
            customsItems=None,
            nonDelivery=""
            ):
        self.contents = contents
        self.customsItems = customsItems
        self.nonDelivery = nonDelivery


class ItemOption(BaseModel):
    def __init__(
            self,
            name="",
            value=""
            ):
        self.name = name
        self.value = value


class OrderItem(BaseModel):
    def __init__(
            self,
            orderItemId=0,
            lineItemKey="",
            sku="",
            name="",
            imageUrl="",
            weight=None,
            quantity=0,
            unitPrice=0,
            taxAmount=0,
            shippingAmount=0,
            warehouseLocation="",
            options=None,
            productId=0,
            fulfillmentSku="",
            adjustment=False,
            upc="",
            createDate="",
            modifyDate=""
            ):
        self.orderItemId = orderItemId
        self.lineItemKey = lineItemKey
        self.sku = sku
        self.name = name
        self.imageUrl = imageUrl
        self.weight = weight
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.taxAmount = taxAmount
        self.shippingAmount = shippingAmount
        self.warehouseLocation = warehouseLocation
        self.options = options
        self.productId = productId
        self.fulfillmentSku = fulfillmentSku
        self.adjustment = adjustment
        self.upc = upc
        self.createDate = createDate
        self.modifyDate = modifyDate


class ProductCategory(BaseModel):
    def __init__(
            self,
            categoryId=0,
            name=""
            ):
        self.categoryId = categoryId
        self.name = name


class ProductTag(BaseModel):
    def __init__(
            self,
            tagId=0,
            name=""
            ):
        self.tagId = tagId
        self.name = name


class ProductType(BaseModel):
    def __init__(
            self,
            productTypeId=0,
            name="",
            weightOz=0,
            length=0,
            width=0,
            height=0,
            defaultCarrierCode="",
            defaultServiceCode="",
            defaultPackageCode="",
            defaultIntlCarrierCode="",
            defaultIntlServiceCode="",
            defaultIntlPackageCode="",
            customsDescription="",
            customsValue="",
            customsTariffNo="",
            customsCountryCode="",
            noCustoms=False
            ):
        self.productTypeId = productTypeId
        self.name = name
        self.weightOz = weightOz
        self.length = length
        self.width = width
        self.height = height
        self.defaultCarrierCode = defaultCarrierCode
        self.defaultServiceCode = defaultServiceCode
        self.defaultPackageCode = defaultPackageCode
        self.defaultIntlCarrierCode = defaultIntlCarrierCode
        self.defaultIntlServiceCode = defaultIntlServiceCode
        self.defaultIntlPackageCode = defaultIntlPackageCode
        self.customsDescription = customsDescription
        self.customsValue = customsValue
        self.customsTariffNo = customsTariffNo
        self.customsCountryCode = customsCountryCode
        self.noCustoms = noCustoms


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
            productCategory=None,
            productType=None,
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
            tags=None
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


class Weight(BaseModel):
    def __init__(
            self,
            value=0,
            units="",
            WeightUnits=0
            ):
        self.value = value
        self.units = units
        self.WeightUnits = WeightUnits
