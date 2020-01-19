from flask import Flask
app = Flask(__name__)
import time
import pyfirmata
#AURDINO IDE USE SERVOFIRMATA

board = pyfirmata.Arduino('COM8')

right = board.get_pin('d:9:s')

right.write(0)

@app.route("/")
def hello_world():
   return "hello 1"
   
@app.route("/update")
def update():
    right.write(120)
    time.sleep(2)
    right.write(0)
    
    return "helllllloooooo"

if __name__ == "__main__":
   app.run()