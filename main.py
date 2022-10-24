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
    selection = GetIntMenyInput("KASSA \n1. Ny Kund \n2. Avsluta\n",1,2)
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

def GetNr():
    # with open("counter.txt","w") as counter:
    #     for currentCounter in counter:
    #         IntCounter = int(currentCounter)
    #         IntCounter = IntCounter + 1
    #         CurrentCounter = str(IntCounter)
    #         counter.write(CurrentCounter)
            return 1
        
def FindProduct(allProducts, ProductID):
    for prod in allProducts:
        if prod.GetProductID() == ProductID:
            return prod
    return None

def NewReceipt(allProducts):
    receipt = Receipt()
    while True:
        print(f"Kvitto: #{GetNr()} {GetTime()}")
        for row in receipt.GetReceiptRows():
            print(f"{row.GetName()} - {row.GetCount()} * {row.GetPerPrice()} = {row.GetRowTotal()}")
        print(receipt.GetTotal())
        #try:    
        newPurchase = (input("Buy item or pay "))
        if newPurchase.lower == "pay":
            with open(f"RECEIPT_{GetDate()}.txt","a") as Kvittot:
                pass
        else:
            #try:
                splitPurchase = newPurchase.split(" ")
                prod = FindProduct(allProducts,splitPurchase[0])
                if prod == None:
                    print("Produkten finns inte!")
                else:
                    receipt.Add(prod.GetName(), int(splitPurchase[1]),prod.GetPrice(),splitPurchase[0])
                #except:
                   # print("Nu vart det fel.1")
                    
        #except:
           # print("Nu vart det fel.2")
        

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
        break
    