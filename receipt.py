from datetime import datetime
class ReceiptRow:
    def __init__(self,productName:str, count:int, perPrice:int,productCode) -> None:
        self.__ProductCode = productCode
        self.__ProductName = productName
        self.__Count = count
        self.__PerPrice = perPrice
    def GetProductCode(self):
        return self.__ProductCode
    def GetName(self):
        return self.__ProductName
    def GetCount(self):
        return self.__Count
    def GetPerPrice(self):
        return self.__PerPrice
    def AddCount(self, count):
        self.__Count = self.__Count + count
    def GetRowTotal(self):
        return self.__Count * self.__PerPrice

class Receipt:
    def __init__(self) -> None:
        self.__Datum = datetime.now
        self.__ReceiptRows = []
    def GetReceiptRows(self):
        return self.__ReceiptRows
    def checkExisting(self):
        pass
    def GetTotal(self):
        sum = 0
        for row in self.__ReceiptRows:
            sum = sum + row.GetRowTotal()
        return sum
    def Add(self, productName,count,perPrice,productCode):
        receiptRow = ReceiptRow(productName,count,perPrice,productCode)
        for row in self.__ReceiptRows:
            if row.GetProductCode() == productCode:
                row.AddCount(count)
                return
        self.__ReceiptRows.append(receiptRow)