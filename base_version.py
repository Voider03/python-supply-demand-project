""" 
in this version, all sellers have 1 stock per day
there is no bargaining 
if seller's ep < buyers's ep, buyer considers the seller 
new expected price are calculated at the end of every day 
three values, id ep and mp 
mp doesn't really matter in this simulation 

"""

import random

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
                if key.sold != True:
                    values[key] = value
                else:
                    continue

            if values:

                chosen_seller = min(values, key=values.get)
                self.bought = True
                self.boughtPrice = chosen_seller.ep
                chosen_seller.sold = True
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
    def __init__(self, Id, mp, ep):
        self.Id = Id

        self.mp = float(mp)
        self.ep = float(ep)

        self.sold = False
    
    def EPcalc(self):
        if self.sold:
            self.ep += 1
        else:
            self.ep -= 1
        
        if self.ep < self.mp:
            self.ep = self.mp

    def cleanup(self):
        self.sold = False

#keeping track of buyers and sellers
buyers = [Buyer(1, 11, 10)]
sellers = [Seller(1, 1, 2)]

#init functions

def printAll(day_num):
    print("-----------------------------------")
    print(f"Day: {day_num}")

    for i in buyers:
        print(f"Buyer {i.Id}'s ep: {i.ep}, bought: {i.bought}, boughtPrice: {i.boughtPrice}")

    print("\n")

    for j in sellers:
        print(f"Seller {j.Id}'s ep: {j.ep}, sold: {j.sold}")

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
    period = int(input("How many days do you want: "))
    for i in range(period):
        day(i)

main()