from datetime import datetime
class ReceiptRow:
    def __init__(self,productName:str, count:int, perPrice:int) -> None:
        self.__ProductName = productName
        self.__Count = count
        self.__PerPrice = perPrice
    def AddCount(self, count):
        self.__Count = self.__Count + count

    def GetRowTotal(self):
        return self.__Count + self.__PerPrice

class Receipt:
    def __init__(self) -> None:
        self.__Datum = datetime.now
        self.__ReceiptRows = []
    def GetReceiptRows(self):
        return self.__ReceiptRows
    def GetTotal(self):
        sum = 0
        for row in self.__ReceiptRows:
            sum = sum + row.GetRowTotal()