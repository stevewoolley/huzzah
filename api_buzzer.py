import socket
import json
from lib import buzzer

BUZZER_PIN = 13
BUZZER = buzzer.Buzzer(BUZZER_PIN)
WEB_PORT = 80
#

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
    html = ""
    return HTML.format(200,
                       HTTP_STATUS_CODES[200],
                       WEB_PAGE.format(html))


def error(code):
    return HTML.format(code,
                       HTTP_STATUS_CODES[code],
                       WEB_PAGE.format("<h1>Error {0} {1}</h1>".format(code, HTTP_STATUS_CODES[code])))


def beep(beeps=2):
    data = json.dumps({'beep': beeps})
    if BUZZER_PIN != 0:
        try:
            BUZZER.beep(int(beeps))
            return JSON.format(200,
                               HTTP_STATUS_CODES[200],
                               length=len(data), json=data)
        except Exception as e:
            return JSON.format(500,
                               HTTP_STATUS_CODES[500],
                               length=len(data), json=data)
    else:
        return JSON.format(500,
                           HTTP_STATUS_CODES[500],
                           length=len(data), json=data)


ROUTES = [
    ("", index),
    ("beep", beep)
]


def dec_strip(txt):
    return txt.decode().rstrip()


if __name__ == "__main__":
    s = socket.socket()
    ai = socket.getaddrinfo("0.0.0.0", WEB_PORT)
    print("Listening on {}".format(ai))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(ai[0][-1])
    s.listen(5)

    while True:
        res = s.accept()
        client_sock = res[0]
        client_addr = res[1]
        client_stream = client_sock
        req = client_stream.readline()
        (req_method, req_url, req_version) = req.split(b" ")
        url = dec_strip(req_url).split('/')
        # print("Method: {}".format(dec_strip(req_method)))
        # print("URL: {}".format(dec_strip(req_url)))
        # print("Version: {}".format(dec_strip(req_version)))
        while True:
            h = client_stream.readline()
            if h == b"" or h == b"\r\n":
                break
            # print(dec_strip(h)) # print more request

        # cycle through routes looking for url
        found = False
        for e in ROUTES:
            pattern = e[0]
            handler = e[1]
            if url[1] == pattern:
                found = True
                break
        if not found:
            client_stream.send(error(404).encode('utf-8'))
        else:
            if len(url) == 2:
                client_stream.send(handler().encode('utf-8'))
            else:
                client_stream.send(handler(url[2]).encode('utf-8'))

        client_stream.close()
