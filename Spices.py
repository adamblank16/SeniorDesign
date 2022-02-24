from LoadCell import *
class Spices:
    def __init__(self, motor, loadcell, spice):
        self.motor = motor
        self.loadcell = loadcell
        self.spice = spice

        match spice:
            case "salt":
                tablespoon = 17.06
                teaspoon = 5.69
            case "basil":
                tablespoon = 1.26
                teaspoon = 0.42

    def dispense(self, amount, type):
        match type:
            case "tablespoon":
                dispense_amount = amount * self.tablespoon
            case "teaspoon":
                dispense_amount = amount * self.teaspoon
        
        while(self.loadcell.get_weight(5)<dispense_amount){
            self.motor.setDirection(180)
        }
        self.motor.setDirection(0)
        
