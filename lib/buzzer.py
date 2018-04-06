import time
import machine


class Buzzer:
    """MicroPython version for Buzzer.
    """

    def __init__(self, pin, on_time=0.06, off_time=0.1, freq=500, duty=1023):
        self.pin = pin
        self.freq = freq
        self.duty = duty
        self.on_time = on_time
        self.off_time = off_time
        self.pwm = machine.PWM(machine.Pin(pin))
        self.pwm.freq(freq)

    def __del__(self):
        self.pwm.deinit()

    def beep(self, beeps=1):
        for _ in range(beeps):
            self.pwm.duty(self.duty)
            time.sleep(self.on_time)
            self.pwm.duty(0)
            time.sleep(self.off_time)


