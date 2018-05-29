import onionGpio

gpioList = [0, 1, 2, 3, 11, 18, 19]

for gpio in gpioList:
	print "Resetting: " + str(gpio)
	onionGpio.OnionGpio(gpio).setOutputDirection(0) 
