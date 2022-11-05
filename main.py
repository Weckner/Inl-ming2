from datetime import datetime
from product import Product
from receipt import Receipt
allProducts = []
with open("products.txt","r") as productFile:
    for product in productFile:
        parts = []
        par = product.split(";")
        for part in par:
            x = part.replace("\n","")
            parts.append(x)
        product = Product(parts[0],parts[1],parts[2],parts[3],parts[4],parts[5],parts[6])
        allProducts.append(product)


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

def AdminMeny():
    selection = GetIntMenyInput("ADMIN \n1. Ändra Produkt \n2. Söka Kvitto \n3. Kampanjer \n4. Tillbaka\n",1,4)
    return selection

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
    while True:
        print(f"Kvitto: {GetTime()}")
        for row in receipt.GetReceiptRows():
            print(f"{row.GetName()} - {row.GetCount()} * {row.GetPerPrice()} = {row.GetRowTotal()}")
        print(receipt.GetTotal())
        try:    
            newPurchase = (input("Buy item or pay e.g 300 1 "))
            if newPurchase == "pay":
                with open(f"RECEIPT_{GetDate()}.txt","a") as kvittot:
                    kvittot.write(f"#{GetNr()}; Kvitto  {GetTime()};")
                    for row in receipt.GetReceiptRows():
                        kvittot.write(f"{row.GetName()};{row.GetCount()};{row.GetPerPrice()};{row.GetRowTotal()}")
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


def AddCampaign():
    produktNr = input("Ange produktnummer: ")
    prod = FindProduct(allProducts,produktNr)
    if prod == None:
        print("Produkten finns inte!")
    else:
        campaignPrice = float(input("Ange Kampanj pris: "))
        prod.setCampaignPrice(campaignPrice)
        startDate = input("När ska det börja? Day Month Year")
        startdateObject = datetime.strptime(startDate, "%d %M %Y")
        prod.setStartDate(startdateObject)
        endDate = input("När ska det sluta? Day Month Year")
        enddateObject = datetime.strptime(endDate, "%d %M %Y")
        prod.setEndDate(enddateObject)
def ChangeProduct():
    produktNr = input("Ange produktnummer: ")
    prod = FindProduct(allProducts,produktNr)
    if prod == None:
        print("Produkten finns inte!")
    else: 
        selection = GetIntMenyInput("Vad vill du ändra? \n1.Namn \n2.Pris",1,2)
        if selection == 1:
            newName = input("Ange nytt namn: ")
            prod.ChangeName(newName)
        elif selection == 2:
            newPrice = input("Ange nytt pris: ")
            prod.ChangePrice(newPrice)
# def SearchReceipt():
#     datum = input("Skriv in datum, year-month-day: ")
#     datetoSearch = datetime.strptime(datum, "%Y-%m-%d")
#     with open (f"RECEIPT_{datetoSearch}.txt","r") as kvittot:
#         receiptSearchList = []
#         for receipt in kvittot:
#             parts = receipt.split(";")
#             product = Receipt(parts[S0],parts[1],parts[2],parts[3],parts[4],parts[5],parts[6])
#             receiptSearchList.append(product)
#         for kvitto in kvittot:
#             print("")
while True:
    selection = HuvudMeny()
    if selection == 1:
        NewReceipt(allProducts)
    elif selection == 2:
        selection = AdminMeny()
        if selection == 1:
            ChangeProduct()
        elif selection == 2:
            SearchReceipt()
        elif selection == 3:
            AddCampaign()
        elif selection == 4: 
            continue
    elif selection == 3:
        with open("products.txt","w") as productFile:
            for product in allProducts:
                    productFile.write(f"{product.GetProductID()};{product.GetName()};{product.GetPrice()};{product.GetPriceType()};{product.GetCampaignPrice()};{product.GetStartDate()};{product.GetEndDate()}\n")
        break
    