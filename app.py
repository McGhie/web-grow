'''

Adapted excerpt from Getting Started with Raspberry Pi by Matt Richardson

Modified by Rui Santos
Complete project details: http://randomnerdtutorials.com

'''


from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import pinboard
app = Flask(__name__)

pins = pinboard.pins

# Set each pin as an output and make it low:
for pin in pins:
    if 'GPIO' in pins[pin]['type']:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      if 'GPIO' in pins[pin]['type']:
          pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('main.html', **templateData)

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


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
