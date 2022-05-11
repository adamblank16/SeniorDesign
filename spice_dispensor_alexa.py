import logging
import os
from flask import *
from flask_ask import *
import RPi.GPIO as GPIO
from LoadCell import LoadCell
from Spices import Spices

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def launch():
	welcome_msg = "welcome to spice dispenser"
	startQuestion = "What spice do you want to dispense and how much?"
	return question(startQuestion)

@ask.intent('dispense_spice', mapping ={'amount': 'amount', 'spices':'spice', 'measurement':'measurement'},
	convert={'amount':int, 'measurement':str, 'spices':str})
def calibration(amount, measurement, spices):
	print(amount)
	print(measurement)
	print(spices)
	loadCell = LoadCell(5,6)
	spice = Spices(loadCell, spices)
	spice.dispense(amount, measurement)
	print("working")
	return statement("Done")

@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
