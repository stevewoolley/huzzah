import machine
import time

led = machine.Pin(0, machine.Pin.OUT)

led.on()
time.sleep(2)
led.off()
