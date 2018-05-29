import onionGpio
import time

pins = [0, 1, 2, 3, 6, 11, 18, 19]
rowGpios = []
colGpios = []

for pin in pins:
    obj = onionGpio.OnionGpio(pin)
    if (pin < 6):
        rowGpios.append(obj)
        rowGpios[-1].setInputDirection()
    else:
        colGpios.append(obj);
        colGpios[-1].setOutputDirection(0)

while 1:
    for i, cGpio in enumerate(colGpios):
        colGpios[0].setOutputDirection(0)
        colGpios[1].setOutputDirection(0)
        colGpios[2].setOutputDirection(0)
        colGpios[3].setOutputDirection(0)
        cGpio.setOutputDirection(1)
        time.sleep(.5)
        for j, rGpio in enumerate(rowGpios):
            print str(pins[j]) + ", " + str(pins[i + 4]) + ": " + str(rGpio.getValue())
