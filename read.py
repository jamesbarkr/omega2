import onionGpio
import time

pin = onionGpio.OnionGpio(0)
status = pin.setInputDirection()

while 1:
	print str(pin.getValue())
	time.sleep(0.1)
