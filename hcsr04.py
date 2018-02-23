import time
import machine


def median(ary):
    return sorted(ary)[int(len(ary) / 2)]


class HCSR04:
    """MicroPython version for Ultrasonic Sensor (HC-SR04).
    """

    def __init__(self, trigger_pin, echo_pin, iterations=5, rounding_digits=2):
        self.trigger = machine.Pin(trigger_pin, mode=machine.Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = machine.Pin(echo_pin, mode=machine.Pin.IN, pull=None)
        self.iterations = iterations
        self.rounding_digits = rounding_digits
        self.echo_timeout_us = 500 * 2 * 30

    def distance(self):
        """Return distance in centimeters.

        :return: Distance in centimeters.
        :rtype: float
        """
        results = []
        for i in range(self.iterations):
            self.trigger.value(0)
            time.sleep(0.00005)
            self.trigger.value(1)
            time.sleep(0.0001)
            self.trigger.value(0)
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            val = (pulse_time / 2) / 29.1
            print("pulse time: {}".format(val))
            results.append(val)
        print("median: {}".format(round(median(results), self.rounding_digits)))
        return round(median(results), self.rounding_digits)
