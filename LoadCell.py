import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711

class LoadCell:
	def __init__(self, data, clk):
		global hx
		self.data = data #the data pin on hx711
		self.clk = clk #the clk pin on hx711
		hx = HX711(self.data, self.clk)
		hx.set_reading_format("MSB", "MSB")
		hx.set_reference_unit(1)
		hx.reset()
		hx.tare()
		print("Tare done! Add weight now...")
		print("ready to calibrate in 5") 
		time.sleep(5)
		calibrate()
		print(referenceUnit)
		print("remove weight")
		time.sleep(5)
		hx.set_reference_unit(referenceUnit)
		hx.reset()
		hx.tare()
		
	def cleanAndExit():
		print("Cleaning...")
		
		if not EMULATE_HX711:
			GPIO.cleanup()
			
		print("Bye!")
		sys.exit()
		
	def calibrate():
		global referenceUnit
		numList = []
		total = 0
		while (len(numList) < 21):
			numList.append(hx.get_weight(5))
		for i in numList:
			total += i
		referenceUnit = ((total/len(numList))/100)
	
