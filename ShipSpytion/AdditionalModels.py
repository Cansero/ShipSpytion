from .BaseModel import BaseModel
from .SubModels import Address, Weight, Dimensions, AdvancedOptions, OrderItem, InsuranceOptions


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
            orderId=0,
            orderKey="",
            userId="",
            orderNumber="",
            createDate="",
            shipDate="",
            shipmentCost=0,
            insuranceCost=0,
            trackingNumber="",
            isReturnLabel=False,
            batchNumber="",
            carrierCode="",
            serviceCode="",
            packageCode="",
            confirmation="",
            warehouseId=0,
            voided=False,
            voidDate="",
            marketplaceNotified=False,
            notifyErrorMessage="",
            shipTo=None,
            weight=None,
            dimensions=None,
            insuranceOptions=None,
            advancedOptions=None,
            shipmentItems=None,
            labelData="",
            formData=None
            ):
        self.shipmentId = shipmentId
        self.orderId = orderId
        self.orderKey = orderKey
        self.userId = userId
        self.orderNumber = orderNumber
        self.createDate = createDate
        self.shipDate = shipDate
        self.shipmentCost = shipmentCost
        self.insuranceCost = insuranceCost
        self.trackingNumber = trackingNumber
        self.isReturnLabel = isReturnLabel
        self.batchNumber = batchNumber
        self.carrierCode = carrierCode
        self.serviceCode = serviceCode
        self.packageCode = packageCode
        self.confirmation = confirmation
        self.warehouseId = warehouseId
        self.voided = voided
        self.voidDate = voidDate
        self.marketplaceNotified = marketplaceNotified
        self.notifuErrorMessage = notifyErrorMessage
        self.shipTo = Address() if shipTo is None else shipTo
        self.weight = Weight() if weight is None else weight
        self.dimensions = Dimensions() if dimensions is None else dimensions
        self.insuranceOptions = InsuranceOptions() if insuranceOptions is None else insuranceOptions
        self.advancedOptions = AdvancedOptions() if advancedOptions is None else advancedOptions
        self.shipmentItems = [OrderItem()] if shipmentItems is None else shipmentItems
        self.labelData = labelData
        self.formData = formData


class Store(BaseModel):
    def __init__(
            self,
            storeId=0,
            storeName="",
            marketplaceId=0,
            marketplaceName="",
            accountName="",
            email="",
            integrationUrl="",
            active=False,
            companyName="",
            phone="",
            publicEmail="",
            website="",
            refreshDate="",
            lastRefreshAttempt="",
            createDate="",
            modifyDate="",
            autoRefresh=False,
            ):
        self.storeId = storeId
        self.storeName = storeName
        self.marketplaceId = marketplaceId
        self.marketplaceName = marketplaceName
        self.accountName = accountName
        self.email = email
        self.integrationUrl = integrationUrl
        self.active = active
        self.companyName = companyName
        self.phone = phone
        self.publicEmail = publicEmail
        self.website = website
        self.refreshDate = refreshDate
        self.lastRefreshAttempt = lastRefreshAttempt
        self.createDate = createDate
        self.modifyDate = modifyDate
        self.autoRefresh = autoRefresh


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
            page=0,
            pageSize=500
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
        self.page = page if page else 1
        self.pageSize = pageSize if 0 < pageSize < 501 else 500


class ListShipmentsOptions(BaseModel):
    def __init__(
            self,
            recipientName="",
            recipientCountryCode="",
            orderNumber="",
            orderId="",
            carrierCode="",
            serviceCode="",
            trackingNumber="",
            customsCountryCode="",
            createDateStart="",
            createDateEnd="",
            shipDateStart="",
            shipDateEnd="",
            voidDateStart="",
            voidDateEnd="",
            storeId=0,
            includeShipmentItems=False,
            sortBy="",
            sortDir="",
            page=0,
            pageSize=0
            ):
        self.recipientName = recipientName
        self.recipientCountrCode = recipientCountryCode
        self.orderNumber = orderNumber
        self.orderId = orderId
        self.carrierCode = carrierCode
        self.serviceCode = serviceCode
        self.trackingNumber = trackingNumber
        self.customsCountryCode = customsCountryCode
        self.createDateStart = createDateStart
        self.createDateEnd = createDateEnd
        self.shipDateStart = shipDateStart
        self.shipDateEnd = shipDateEnd
        self.voidDateStart = voidDateStart
        self.voidDateEnd = voidDateEnd
        self.storeId = storeId
        self.includeShipmentItems = includeShipmentItems
        self.sortBy = sortBy
        self.sortDir = sortDir
        self.page = page
        self.pageSize = pageSize


class ListStoresOptions(BaseModel):
    def __init__(
            self,
            showInactive=False,
            marketplaceId=0,
            ):
        self.showInactive = showInactive
        self.marketplaceId = marketplaceId


class MarkShippedOptions(BaseModel):
    def __init__(
            self,
            carrierCode="",
            shipDate="",
            trackingNumber="",
            notifyCustomer=True,
            notifySalesChannel=False,
            ):
        self.carrierCode = carrierCode
        self.shipDate = shipDate
        self.trackingNumber = trackingNumber
        self.notifyCustomer = notifyCustomer
        self.notifySalesChannel = notifySalesChannel
