import random

#keeping track of buyers and sellers
buyers = []
sellers = []

#classes of entities
class Buyer:
    def __init__(self, Id, mp, ep, stock, dp, bp):
        self.Id = Id

        self.mp = float(mp)
        self.ep = float(ep)

        self.sp = 0

        self.dp = dp
        self.bp = bp

        self.stock = stock
        self.daily_stock = self.stock

        self.boughtPrice = 0
        self.shopsVisited = {}

    def buy(self):
        if self.shopsVisited:

            chosen_seller = min(self.shopsVisited, key=self.shopsVisited.get)
            self.daily_stock -= 1
            self.boughtPrice = self.shopsVisited[chosen_seller]
            chosen_seller.daily_stock -= 1

            if chosen_seller.daily_stock == 0:
                self.shopsVisited.pop(chosen_seller)

    def EPcalc(self):
        if self.daily_stock <= self.stock / 2:
            self.ep -= 1
        else:
            self.ep += 1
        
        if self.ep > self.mp:
            self.ep = self.mp
        if self.ep <= 0:
            self.ep = 1
    
    def cleanup(self):
        self.shopsVisited = {}
        self.daily_stock = self.stock
        self.boughtPrice = 0


class Seller:
    def __init__(self, Id, mp, ep, stock, dp, bp):
        self.Id = Id

        self.mp = float(mp)
        self.ep = float(ep)

        self.dp = float(dp)
        self.bp = float(bp)

        self.stock = stock

        self.daily_stock = self.stock
    
    def EPcalc(self):
        if self.daily_stock <= self.stock / 2:
            self.ep += 1
        else:
            self.ep -= 1
        
        if self.ep < self.mp:
            self.ep = self.mp

    def cleanup(self):
        self.daily_stock = self.stock


#init functions
def detBuy(numBuyers):
    for i in range(numBuyers):

        ep = float(input(f"\nEnter Buyer {i} ep: "))
        mp = float(input(f"Enter Buyer {i} mp: "))
        stock = int(input(f"Enter Buyer {i} stock: "))
        dp = float(input(f"Enter Buyer {i} discount percentage: "))
        bp = float(input(f"Enter Buyer {i} maximum discount percentage: "))

        buyers.append(Buyer(i, mp, ep, stock, dp, bp))

def detSel(numSellers):
    for i in range(numSellers):

        ep = float(input(f"\nEnter Seller {i} ep: "))
        mp = float(input(f"Enter Seller {i} mp: "))
        stock = int(input(f"Enter Seller {i} stock: "))
        dp = float(input(f"Enter Buyer {i} discount percentage: "))
        bp = float(input(f"Enter Buyer {i} maximum discount percentage: "))

        sellers.append(Seller(i, mp, ep, stock, dp, bp))

def init():
    numBuyers = int(input("Enter number of buyers you want: "))
    numSellers = int(input("Enter number of sellers you want: "))

    detBuy(numBuyers)
    detSel(numSellers)

    time = int(input("How many days: "))

    return time

def printAll(day_num):
    print("-----------------------------------")
    print(f"Day: {day_num}")

    for i in buyers:
        print(f"Buyer {i.Id}'s ep: {i.ep}, stock: {i.daily_stock}, boughtPrice: {i.boughtPrice},")

    print("\n")

    for j in sellers:
        print(f"Seller {j.Id}'s ep: {j.ep}, stock: {j.daily_stock}")

    print("-----------------------------------")


#main day functions
def day(day_num):
    buyersStart = random.randint(0, len(buyers) - 1)
    buyersRotated = buyers[buyersStart:] + buyers[:buyersStart]

    for i in buyersRotated:
        sellersStart = random.randint(0, len(sellers) - 1)
        sellersRotated = sellers[sellersStart:] + sellers[:sellersStart]

        for j in sellersRotated:
          if j.daily_stock == 0:
              continue
          if j.ep <= i.ep:
            i.shopsVisited[j] = j.ep
          elif j.ep > i.ep and ((j.ep-i.ep)*(1-(i.dp-j.dp))) < i.bp * i.ep:
            i.shopsVisited[j] = i.ep + ((j.ep-i.ep)*(1-(i.dp-j.dp)))
          elif j.ep > i.mp:
              break

        while i.daily_stock != 0 and i.shopsVisited:
         i.buy()

        i.EPcalc()

    for s in sellers:
        s.EPcalc()

    printAll(day_num)
    newDay()

def newDay():
    for i in buyers:
        i.cleanup()
    for i in sellers:
        i.cleanup()

#starter function
def main():
    period = init()
    for i in range(period):
        day(i)

main()