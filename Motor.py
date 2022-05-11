import RPi.GPIO as GPIO
import time

class Motor:
	def __init__(self, gpio):
		#GPIO.setmode(GPIO.BOARD)
                #GPIO.cleanup()
                #GPIO.setmode(GPIO.BCM)
                self.gpio = gpio #the gpio number of the motor
		self.fPWM = 50  # Hz (not higher with software PWM)
		self.a = 10
		self.b = 2
		
		self.lastDuty = 6

		self.currentDuty = 2
                try:
                    self.setup()
                except:
                    pass
		
	def setup(self):
		#GPIO.setmode(GPIO.BOARD)
                #GPIO.cleanup()
                #GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.gpio, GPIO.OUT)
		self.pwm = GPIO.PWM(self.gpio, self.fPWM)
		self.pwm.start(self.currentDuty)

        def setDirection(self, direction):
		print(self.currentDuty)
		self.pwm.ChangeFrequency(self.fPWM)
		self.pwm.start(self.currentDuty)
		#direction = input("Enter Direction")   
		self.duty = direction / 18.0 + self.b
		self.currentDuty = self.duty
		print (self.duty)
		GPIO.output(self.gpio,True)
		self.pwm.ChangeDutyCycle(self.duty)
		print "direction =", direction, "-> duty =", self.duty
		time.sleep(1) # allow to settle
		self.pwm.stop()
