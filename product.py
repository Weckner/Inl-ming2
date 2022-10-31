class Product:
    def __init__(self,productID:int, name:str, price:int, priceType:str) -> None:
        self.__ProductID = productID
        self.__Name = name
        self.__Price = price
        self.__priceType = priceType
    def GetName(self):
        return self.__Name
    def GetPrice(self):
        return float(self.__Price)
    def GetProductID(self):
        return self.__ProductID    
    def GetPriceType(self):
        return self.__priceType    
    def ChangeName(self,newName):
        self.__Name = newName
    def ChangePrice(self, newPrice):
        self.__Price = newPrice