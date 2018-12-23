'''
Original Code Source Start
Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson
Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

Modified by Argyll McGhie
Source code: https://github.com/McGhie/web-grow

'''
import os
from flask import Flask, render_template, redirect, url_for, request

from flask import flash
#from flask.ext.socketio import SocketIO, emit
import datetime
#import threading

#from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event


import read_arduino
#import moment
#from py import clock as clock
#from py import servo as servo

DEBUG = True
#Su_Mo_Tu_We_Th_Fr_Sa


def log(s):
    if DEBUG:
        print (s)
if (os.uname()[4].startswith("arm")): #check if system is pi if not use fake pins
    import RPi.GPIO as GPIO
    import pinboard
    DEBUG = False
else:
    #()'you are not using a raspberryPi, debug strings are set')
    from debugFolder import gpioString as GPIO
    from debugFolder import debugStrings as pinboard

    GPIO = pinboard.GPIO

print("HARDWARE: " + (os.uname()[4]) )



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webgrowdev.sqlite3'
#app.config['SECRET_KEY'] = "random string"
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#socketio = SocketIO(app)






#////////////////////////////////////////////////////////////

pins = pinboard.pins

# Set each pin as an output and make it low:
for pin in pins:
    if 'GPIO' in pins[pin]['type']:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

globalData = {
  # 'now':moment.now().format("DD-MM-YYYY"),
  # 'pumpon': clock.pumpon,
   #'pumpoff': clock.pumpoff,
   'pins' : pins

   }


#/////////////////////////////
#random number Generator Thread
thread = Thread()
thread_stop_event = Event()

pump_thread = Thread()
pump_thread_event = Event()

print ("Pump thread is: " + str(pump_thread_event.isSet()))


\

@app.route("/index")
def main():

   # For each pin, read the pin state and store it in the pins dictionary:
   #log(route("/"))
   for pin in pins:
      if 'GPIO' in pins[pin]['type']:
          pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'now':globalData['now'],
      'pins' : pins

      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('index.html', **templateData)










@app.route("/index/servo/<duration>")
def servoAction(duration):
    servo.timer(duration)
    for pin in pins:
       if 'GPIO' in pins[pin]['type']:
           pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
    templateData = {
       'now':globalData['now'],
       'pins' : pins

       }
   # Pass the template data into the template main.html and return it to the user
    return render_template('index.html', **templateData)


@app.route("/index/<changePin>/<action>")
def indexaction(changePin, action):
     # For each pin, read the pin state and store it in the pins dictionary:
  #log(route("/"))
  if not pump_thread_event.isSet():
      if action == "ten":
          GPIO.output(12, GPIO.HIGH)
          print("the pump has started")
          pump_thread_event.set()


  for pin in pins:
     if 'GPIO' in pins[pin]['type']:
         pins[pin]['state'] = GPIO.input(pin)
  # Put the pin dictionary into the template data dictionary:
  templateData = {
     #'now':moment.now().format("DD-MM-YYYY"),
     'pins' : pins

     }






  # Pass the template data into the template main.html and return it to the user
  return render_template('index.html', **templateData)

@app.route("/controls")
def controls():
   # For each pin, read the pin state and store it in the pins dictionary:
   #log(route("/"))
   for pin in pins:
      if 'GPIO' in pins[pin]['type']:
          pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins,

      }

   # Pass the template data into the template main.html and return it to the user
   return render_template('controls.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device type for the pin being changed:
   devicetype = pins[changePin]['type']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + devicetype + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + devicetype + " off."
      #hardcoded direction/flip pins 12 and 16
   if action == "left":
      GPIO.output(12, GPIO.LOW)
      GPIO.output(16, GPIO.HIGH)
      message = "Turned Motor Direction"
   if action == "right":
      GPIO.output(16, GPIO.LOW)
      GPIO.output(12, GPIO.HIGH)
      message = "Turned Motor Direction"
   if action == "ten":
      GPIO.output(12, GPIO.HIGH)
      print("the pump has started")
      pump_thread_event.set()



   # For each pin, read the pin state and store it in the pins dictionary:


   for pin in pins:
      if 'GPIO' in pins[pin]['type']:
         pins[pin]['state'] = GPIO.input(pin)


   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)



# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/'))
    return render_template('login.html', error=error)

@app.route('/datas', methods=['GET'])
def show_all():
    return render_template('datas.html', webgrowdev = webgrowdev.query.all())


@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         data = webgrowdev(request.form['name'], request.form['city'],request.form['addr'])

         db.session.add(data)
         db.session.commit()

         flash('Record was successfully added')
         return redirect(url_for('datas'))
   return render_template('new.html')


@app.route('/conditions', methods = ['GET', 'POST'])
def arduino():
   if (DEBUG):
       read_arduino.getfromlaptop()
   else:
       read_arduino.getfrompi()
   return render_template('conditions.html')

@app.route("/conditions/<action>")
def edit(action):
   if action == "clear":
       read_arduino.clearData()
   if action == "readfrompi":
       read_arduino.getfrompi()

   return render_template('conditions.html')


if __name__ == "__main__":




   app.run(host='0.0.0.0', port=8080, debug=True)
