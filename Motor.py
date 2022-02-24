import RPi.GPIO as GPIO
import time

class Motor:
	def __init__(self, gpio):
		self.gpio = gpio #the gpio number of the motor
		self.fPWM = 50  # Hz (not higher with software PWM)
		self.a = 10
		self.b = 2
		setup()
		
	def setup(self):
		global pwm
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.gpio, GPIO.OUT)
		pwm = GPIO.PWM(self.gpio, seld.fPWM)
		pwm.start(10)

	def setDirection(self, direction):
		#direction = input("Enter Direction")   
		duty = direction / 18 + self.b
		GPIO.output(self.gpio,True)
		pwm.ChangeDutyCycle(duty)
		print "direction =", direction, "-> duty =", duty
		time.sleep(1) # allow to settle
