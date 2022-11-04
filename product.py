class Product:
    def __init__(self,productID:int, name:str, price:float, priceType:str,campaignPrice, startDate, endDate) -> None:
        self.__ProductID = productID
        self.__Name = name
        self.__Price = price
        self.__priceType = priceType
        self.__StartDate = startDate
        self.__EndDate = endDate
        self.__CampaignPrice = campaignPrice
    def GetName(self):
        return self.__Name
    def GetPrice(self):
        return float(self.__Price)
    def GetProductID(self):
        return self.__ProductID    
    def GetPriceType(self):
        return self.__priceType
    def GetStartDate(self):
        return self.__StartDate
    def GetEndDate(self):
        return self.__EndDate
    def GetCampaignPrice(self):
        return self.__CampaignPrice    
    def ChangeName(self,newName):
        self.__Name = newName
    def ChangePrice(self, newPrice):
        self.__Price = newPrice
    def setCampaignPrice(self, newCampaignPrice):
        self.__CampaignPrice = newCampaignPrice
    def setStartDate(self, newStartDate):
        self.__StartDate = newStartDate
    def setEndDate(self, newEndDate):
        self.__EndDate = newEndDate