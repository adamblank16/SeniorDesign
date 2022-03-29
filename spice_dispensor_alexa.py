import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import RPi.GPIO as GPIO
from Dispensor import LoadCell

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def startup():
	welcome_msg = render_template('welcome')
	return statement(welcome_msg)
	return question("Are you ready to calibrate?")

@ask.intent("YesIntent")
def calibration():
	loadCell = LoadCell(5,6)
	return question("What do you want to dispense?")

@ask.intent(
	
