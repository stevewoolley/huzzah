import utils
import dht
import machine
import esp
import time

DHT_PIN = 14

dht22 = dht.DHT22(machine.Pin(DHT_PIN))

time.sleep(5)

try:
    dht22.measure()
    aws_config = utils.get_config('/config/aws_info.json')
    result = utils.iot_put(aws_config, {'temperature': dht22.temperature(), 'humidity': dht22.humidity()})
    print("iot put result: {}".format(result))
except Exception as e:
    print("exception {}".format(e))

esp.deepsleep(300 * 1000000)
