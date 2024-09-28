class BaseModel:
    def update(self, ref: dict):
        if not isinstance(ref, dict):
            return
        for k, v in ref.items():
            if isinstance(v, dict):
                obj = getattr(self, k)
                obj.update(v)
            else:
                setattr(self, k, v)

    def as_dict(self):
        variables = vars(self)
        to_return = variables.copy()
        for k, v in variables.items():
            if isinstance(v, BaseModel):
                to_return[k] = v.as_dict()
        return to_return


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
        self.mergedIds = [] if mergedIds is None else mergedIds
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
