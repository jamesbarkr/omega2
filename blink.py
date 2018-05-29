import onionGpio
import time

sleepTime = 0.01

gpioPins = [0, 1, 2, 3]
gpioObjects = []
ledValue = 1

for pin in gpioPins:
	gpioObjects.append(onionGpio.OnionGpio(pin))
	gpioObjects[-1].setOutputDirection(0)

while 1:
    for gpio in gpioObjects:
	gpio.setValue(ledValue)
	time.sleep(sleepTime)

    if ledValue == 1:
	ledValue = 0
    else:
        ledValue = 1

    time.sleep(sleepTime)
