from LoadCell import LoadCell
from Motor import Motor

class Spices:
    def __init__(self, loadcell, spice):
        self.loadcell = loadcell
        self.spice = spice

        if (self.spice == "salt"):
            self.tablespoon = 17.06
            self.teaspoon = 5.69
            self.motor = Motor(22)
        if (self.spice == "pepper"):
            self.tablespoon = 6.90
            self.teaspoon = 2.30
            self.motor = Motor(27)
        if (self.spice == "basil"):
            self.tablespoon = 1.26
            self.teaspoon = 0.42
            self.motor = Motor(27)
                

    def dispense(self, amount, tab): ##the +2 is taking account for the cup
        if (tab =="tablespoon"):
            if (amount < 1):
                dispense_amount = amount * self.tablespoon
                angle = 12
            else:
                dispense_amount = amount * self.tablespoon - 6
                angle = 8
        if (tab == "teaspoon"):
            if (amount < 1):
                dispense_amount = amount * self.teaspoon 
                angle = 8
            else:
                dispense_amount = amount * self.teaspoon - 3.7
                angle = 8
        if (tab == "grams"):
            if (amount <= 3):
                dispense_amount = amount 
                angle = 8
            else:
                dispense_amount = amount - 3.7
                angle = 8
        
        self.motor.setDirection(angle)
        
        while(self.loadcell.readWeight()<dispense_amount):
            continue 

        self.motor.setDirection(0)

