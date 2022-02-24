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
		self.calibrate()
		print(referenceUnit)
		print("remove weight")
		time.sleep(5)
		hx.set_reference_unit(referenceUnit)
		hx.reset()
		hx.tare()
		
	def cleanAndExit(self):
		print("Cleaning...")
		
		if not EMULATE_HX711:
			GPIO.cleanup()
			
		print("Bye!")
		sys.exit()
		
	def calibrate(self):
		global referenceUnit
		numList = []
		total = 0
		while (len(numList) < 21):
			numList.append(hx.get_weight(5))
		for i in numList:
			total += i
		referenceUnit = ((total/len(numList))/100)
		
	def readWeight(self):
		print(hx.get_weight(5))
		return hx.get_weight(5)
	
class Motor:
	def __init__(self, gpio):
		self.gpio = gpio #the gpio number of the motor
		self.fPWM = 50  # Hz (not higher with software PWM)
		self.a = 10
		self.b = 2
		self.setup()
		
	def setup(self):
		global pwm
		#GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.gpio, GPIO.OUT)
		pwm = GPIO.PWM(self.gpio, self.fPWM)
		pwm.start(10)

	def setDirection(self, direction):
		#direction = input("Enter Direction")   
		duty = direction / 18 + self.b
		GPIO.output(self.gpio,True)
		pwm.ChangeDutyCycle(duty)
		print "direction =", direction, "-> duty =", duty
		time.sleep(1) # allow to settle


loadCell = LoadCell(5,6)
motor = Motor(17)

motor.setDirection(0)

while(loadCell.readWeight() < 10):
	motor.setDirection(180)

motor.setDirection(0)
loadCell.cleanAndExit()

