""" 
in this version, all sellers have variable stock per day
there is no bargaining 
if seller's ep < buyers's ep, buyer considers the seller 
new expected price are calculated at the end of every day 
4 values, id ep and mp and stock
mp doesn't really matter in this simulation 
at the start the user will type in the amount of buyers and amount of sellers 
user then assigns the values of each entity
and also stock resets every day

"""

import random

#keeping track of buyers and sellers
buyers = []
sellers = []

#classes of entities
class Buyer:
    def __init__(self, Id, mp, ep):
        self.Id = Id

        self.mp = float(mp)
        self.ep = float(ep)

        self.bought = False
        self.boughtPrice = 0
        self.shopsVisited = {}

    def buy(self):
        if self.shopsVisited:
            values = {}

            for key, value in self.shopsVisited.items():
                if key.daily_stock != 0:
                    values[key] = value
                else:
                    continue

            if values:

                chosen_seller = min(values, key=values.get)
                self.bought = True
                self.boughtPrice = chosen_seller.ep
                chosen_seller.daily_stock -= 1
        else:
            self.bought = False

    def EPcalc(self):
        if self.bought:
            self.ep -= 1
        else:
            self.ep += 1
        
        if self.ep > self.mp:
            self.ep = self.mp
    
    def cleanup(self):
        self.shopsVisited = {}
        self.bought = False
        self.boughtPrice = 0


class Seller:
    def __init__(self, Id, mp, ep, stock):
        self.Id = Id

        self.mp = float(mp)
        self.ep = float(ep)

        self.stock = stock

        self.daily_stock = self.stock
    
    def EPcalc(self):
        if self.daily_stock < self.stock:
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

        buyers.append(Buyer(i, mp, ep))

def detSel(numSellers):
    for i in range(numSellers):

        ep = float(input(f"\nEnter Seller {i} ep: "))
        mp = float(input(f"Enter Seller {i} mp: "))
        stock = int(input(f"Enter Seller {i} stock: "))

        sellers.append(Seller(i, mp, ep, stock))

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
        print(f"Buyer {i.Id}'s ep: {i.ep}, bought: {i.bought}, boughtPrice: {i.boughtPrice}")

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
            if j.ep <= i.ep:
                i.shopsVisited[j] = j.ep

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