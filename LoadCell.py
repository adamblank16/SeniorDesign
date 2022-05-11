import time
import sys
import RPi.GPIO as GPIO
from hx711 import HX711

class LoadCell:
	def __init__(self, data, clk):
		GPIO.cleanup()
		#GPIO.setmode(GPIO.BOARD)
		
		self.data = data #the data pin on hx711
		self.clk = clk #the clk pin on hx711
		self.hx = HX711(self.data, self.clk)
		self.hx.set_reading_format("MSB", "MSB")
		self.hx.set_reference_unit(5689.93)
		self.hx.reset()
                #print("put bowl on scale")
                #time.sleep(5)
		#self.hx.tare()
		#print("Tare done! Add weight now...")
		#print("ready to calibrate in 5") 
		#time.sleep(15)
		#twentFive = self.calibrate(25)
		#print(twentFive)
		#print("remove weight")
		#time.sleep(15)
		#self.hx.reset()
		#self.hx.tare()
		#print("Tare done! Add weight now...")
		#print("ready to calibrate in 5") 
		#time.sleep(15)
		#fifty = self.calibrate(50)
		#print(fifty)
		#print("remove weight")
		#time.sleep(15)
		#self.hx.reset()
		#self.hx.tare()
		#print("Tare done! Add weight now...")
		#print("ready to calibrate in 5") 
		#time.sleep(15)
		#seventyFive = self.calibrate(75)
		#print(seventyFive)
		#print("remove weight")
		#avg = (twentFive+fifty)/2.0
		#print(avg)
                #self.hx.set_reference_unit(avg)
		#time.sleep(15)
		#hx.reset()
		self.hx.tare()
		
	def cleanAndExit():
		print("Cleaning...")
		
		if not EMULATE_HX711:
			GPIO.cleanup()
			
		print("Bye!")
		sys.exit()
		
	def readWeight(self):
		print(self.hx.get_weight(5))
		return self.hx.get_weight(5)
		
	def calibrate(self, weight):
		numList = []
		total = 0
		while (len(numList) < 21):
			numList.append(self.hx.get_weight(5))
		for i in numList:
			total += i
		referenceUnit = ((total/len(numList))/(float)(weight))
		return referenceUnit
	
