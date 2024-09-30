MAY_BE_LIST = ['options', 'items', 'mergedIds']


class BaseModel:
    def update(self, ref: dict):
        if not isinstance(ref, dict):
            return
        for k, v in ref.items():
            if isinstance(v, dict):
                obj = getattr(self, k)
                obj.update(v)
            elif isinstance(v, list):
                if k in MAY_BE_LIST:
                    obj = None
                    match k:
                        case "options":
                            obj = ItemOption()
                        case "items":
                            obj = OrderItem()
                    if len(v) > 0:
                        for item in v:
                            pass  # WARNING: Continue
                    else:
                        setattr(self, k, v)
                else:
                    print("idk what this is")
            else:
                setattr(self, k, v)

    def as_dict(self):
        variables = vars(self)
        to_return = variables.copy()
        for k, v in variables.items():
            if isinstance(v, BaseModel):
                to_return[k] = v.as_dict()
        return to_return


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
            mergedIds=None,  # FIX: List of Ints
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
        self.mergedIds = [0] if mergedIds is None else mergedIds
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
            customsItems=CustomsItems(),
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
            weight=Weight(),
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
        self.options = [ItemOption()] if options is None else options
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
