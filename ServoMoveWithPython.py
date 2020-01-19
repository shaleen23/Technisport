import pyfirmata
#AURDINO IDE USE SERVOFIRMATA
board = pyfirmata.Arduino('COM8')
turret = board.get_pin('d:9:s')
left = board.get_pin('d:9:s')
right = board.get_pin('d:9:s')

right.write(90)
left.write(60)
time.sleep(3)
left.write(90)
time.sleep(3)
right.write(120)
time.sleep(3)
right.write(90)
time.sleep(3)