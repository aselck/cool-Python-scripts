import keyboard
import time

def countdown():
	countdown = 15
	while True:
		if countdown > 0:
			keyboard.write(str(countdown))
			keyboard.send("enter")
			countdown = countdown - 1
			time.sleep(1)
		else:
			break
		

time.sleep(5)
countdown()
