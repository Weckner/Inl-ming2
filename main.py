from datetime import datetime
from product import Product
from receipt import Receipt
allProducts = []
with open("products.txt","r") as productFile:
    for product in productFile:
        parts = product.split(";")
        product = Product(parts[0],parts[1],parts[2],parts[3] )
        allProducts.append(product)
# print(allProducts[0].GetName())
# print(allProducts[0].GetPrice())
# print(allProducts[0].GetPriceType())
# print(allProducts[0].GetProductID())

def HuvudMeny() -> int:
    selection = GetIntMenyInput("KASSA \n1. Ny Kund \n2. Admin \n3. Avsluta\n",1,3)
    return selection
def GetIntMenyInput(menyValA, minValue, maxValue):
    while True:
        try:
            select = int(input(menyValA))
            if select < minValue or select > maxValue:
                print(f"Mata in ett tal mellan {minValue} och {maxValue}: ")
            else:
                break
        except:
           print("Förstår inte vad du menar, försök igen!\n")
    return select

def Admin():
    pass

def GetNr():
    with open("counter.txt","r") as counter:
        for currentCounter in counter:
            intCounter = int(currentCounter)
            intCounter = intCounter + 1
            currentCounter = str(intCounter)
    with open("counter.txt","w") as counter:        
            counter.write(currentCounter)
    return intCounter
        
def FindProduct(allProducts, ProductID):
    for prod in allProducts:
        if prod.GetProductID() == ProductID:
            return prod
    return None

def NewReceipt(allProducts):
    receipt = Receipt()
    receiptNr = GetNr()
    while True:
        print(f"Kvitto: #{receiptNr} {GetTime()}")
        for row in receipt.GetReceiptRows():
            print(f"{row.GetName()} - {row.GetCount()} * {row.GetPerPrice()} = {row.GetRowTotal()}")
        print(receipt.GetTotal())
        try:    
            newPurchase = (input("Buy item or pay e.g 300 1 "))
            if newPurchase == "pay":
                with open(f"RECEIPT_{GetDate()}.txt","a") as kvittot:
                    kvittot.write(f"Kvitto: #{receiptNr} {GetTime()}")
                    for row in receipt.GetReceiptRows():
                        kvittot.write(f"{row.GetName()} - {row.GetCount()} * {row.GetPerPrice()} = {row.GetRowTotal()}")
                    kvittot.write(f"Total = {receipt.GetTotal()}§\n")
                    break
            else:
                try:
                    splitPurchase = newPurchase.split(" ")
                    prod = FindProduct(allProducts,splitPurchase[0])
                    if prod == None:
                        print("Produkten finns inte!")
                    else:
                        receipt.Add(prod.GetName(), int(splitPurchase[1]),prod.GetPrice(),splitPurchase[0])
                except:
                    print("Nu vart det fel.1")
                    
        except:
            print("Nu vart det fel.2")
        

def GetTime():
    date = datetime.now()
    formatedDate = date.strftime("%Y-%m-%d %H:%M:%S")
    return formatedDate

def GetDate():
    date = datetime.now()
    formatedDate = date.strftime("%Y-%m-%d")
    return formatedDate

while True:
    selection = HuvudMeny()
    if selection == 1:
        NewReceipt(allProducts)
    elif selection == 2:
        Admin()
    elif selection == 3:
        break
    