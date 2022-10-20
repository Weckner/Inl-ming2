from datetime import datetime
from produkt import Product
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
    with open("counter.txt","w") as counter:
        for currentCounter in counter:
            int(currentCounter)
            currentCounter = currentCounter + 1
            counter.write(currentCounter)
            return currentCounter
        

def NyttKvitto():
    kvitto = []
    while True:
        print(f"Kvitto: #{GetNr()} {GetTime()}\n{kvitto}")
        try:    
            newPurchase = input("Buy item or pay")
            if newPurchase.lower == "pay":
                with open(f"RECEIPT_{GetDate()}.txt","a") as Kvittot:
                    pass
            else:
                try:
                    
                    kvitto.append()
                except:
                    print("Nu vart det fel.")
                    
        except:
            print("Nu vart det fel.")
        

def GetTime():
    date = datetime.now()
    formatedDate = date.strftime("%Y-%m-%d %H:%M:%S")
    return formatedDate

def GetDate():
    date = datetime.now()
    formatedDate = date.strftime("%Y-%m-%d")
    return formatedDate
banan = Product(300, "Banan",5,"Styck")
while True:
    selection = GetIntMenyInput("KASSA \n1. Ny Kund \n2. Avsluta\n",1,2)
    if selection == 1:
        pass
    elif selection == 2:
        break
    