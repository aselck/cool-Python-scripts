import math
import keyboard
import time

time.sleep(10)

def sender():
	daten = 0
	while True:
		if daten != 100000:
			keyboard.write(str(daten))
			keyboard.send("enter")
			daten = daten + 1
		else:
			break


sender()
