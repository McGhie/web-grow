'''
Original Code Source Start
Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson
Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

Modified by Argyll McGhie
Source code: https://github.com/McGhie/web-grow

'''

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
import read_arduino as ra;


DEBUG = True

def log(s):
    if DEBUG:
        print s

try:
    import RPi.GPIO as GPIO
    import pinboard
except ImportError:
    #raise ImportError('you are not using a raspberryPi, debug strings are set')
    from debugFolder import debugStrings as pinboard
    from debugFolder import gpioString as GPIO
    GPIO = pinboard.GPIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webgrowdev.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)
class webgrowdev(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

   def __init__(self, name, city, addr,pin):
      self.name = name
      self.city = city
      self.addr = addr
      self.pin = pin

db.create_all()







#////////////////////////////////////////////////////////////

pins = pinboard.pins

# Set each pin as an output and make it low:
for pin in pins:
    if 'GPIO' in pins[pin]['type']:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)





@app.route("/index")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   #log(route("/"))
   for pin in pins:
      if 'GPIO' in pins[pin]['type']:
          pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
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
      'pins' : pins
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

@app.route('/data', methods=['GET'])
def show_all():
    log("data page")
    return render_template('data.html', data = webgrowdev)


@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         data = webgrowdev(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])

         db.session.add(data)
         db.session.commit()

         flash('Record was successfully added')
         return redirect(url_for('webgrowdev'))
   return render_template('new.html')

@app.route('/conditions', methods = ['GET', 'POST'])
def arduino():
   return render_template('conditions.html')


if __name__ == "__main__":

   db.create_all()
   app.run(host='0.0.0.0', port=8080, debug=True)
