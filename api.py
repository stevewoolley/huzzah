import socket
import json
import hcsr04
import dht
import machine

HTTP_STATUS_CODES = {200: 'OK',
                     404: 'Not Found',
                     500: 'Internal Server Error',
                     503: 'Service Unavailable'
                     }

WEB_PAGE = """<!DOCTYPE html>
<html>
  <body>
    {0}
  </body>
</html>  
"""

HTML = """HTTP/1.1 {0} {1}
Content-type: text/html; charset=UTF-8

{2}"""

JSON = """HTTP/1.1 {0} {1}
Content-type: text/json
Content-length: {length}

{json}"""


def index():
    hc = hcsr04.HCSR04(13, 16)
    dht22 = dht.DHT22(machine.Pin(2))
    dht22.measure()
    html = "<p>Distance: {} cm</p>".format(hc.distance())
    html += "<p>Temperature: {} C</p>".format(dht22.temperature())
    html += "<p>Humidity: {} %</p>".format(dht22.humidity())
    return HTML.format(200,
                       HTTP_STATUS_CODES[200],
                       WEB_PAGE.format(html))


def distance():
    hc = hcsr04.HCSR04(13, 16)
    data = json.dumps({'distance': hc.distance()})
    return JSON.format(200,
                       HTTP_STATUS_CODES[200],
                       length=len(data), json=data)


def temperature():
    dht22 = dht.DHT22(machine.Pin(2))
    dht22.measure()
    data = json.dumps({'temperature': dht22.temperature()})
    return JSON.format(200,
                       HTTP_STATUS_CODES[200],
                       length=len(data), json=data)


def humidity():
    dht22 = dht.DHT22(machine.Pin(2))
    dht22.measure()
    data = json.dumps({'humidity': dht22.humidity()})
    return JSON.format(200,
                       HTTP_STATUS_CODES[200],
                       length=len(data), json=data)


def error(code):
    return HTML.format(code,
                       HTTP_STATUS_CODES[code],
                       WEB_PAGE.format("<h1>Error {0} {1}</h1>".format(code, HTTP_STATUS_CODES[code])))


ROUTES = [
    ("/", index),
    ("/temperature", temperature),
    ("/distance", distance),
    ("/humidity", humidity)
]

if __name__ == "__main__":
    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(1)

    print("Listening on {}".format(addr))

    while True:
        cl, ai = s.accept()
        print('client connected from {}'.format(ai))
        cl_file = cl.makefile('rwb', 0)
        (method, url, version) = cl_file.readline().split(b" ")
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        found = False
        for e in ROUTES:
            pattern = e[0]
            handler = e[1]
            if url.decode() == pattern:
                found = True
                break
        if not found:
            cl.send(error(404).encode('utf-8'))
        else:
            cl.send(handler().encode('utf-8'))
        # cl.shutdown(socket.SHUT_RDWR)
        cl.close()
