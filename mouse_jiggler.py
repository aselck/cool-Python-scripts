import mouse
import time

while True:
	mouse.move(100, 100, absolute=False, duration=0.2)
	time.sleep(15)
	mouse.move(-100, -100, absolute=False, duration=0.2)
	time.sleep(15)
