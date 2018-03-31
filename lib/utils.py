def iot_put(aws_config, data):
    import json
    import trequests as requests
    import awsiot_sign
    post_body = {'state': {'reported': {}}}
    for k, v in data.items():
        post_body['state']['reported'][k] = v
    post_body_str = json.dumps(post_body)
    print('{}'.format(post_body_str))
    request_dict = awsiot_sign.request_gen(
        aws_config['endpt_prefix'],
        thing_id(),
        aws_config['akey'],
        aws_config['skey'],
        get_date_time_stamp(),
        method='POST',
        region=aws_config['region'],
        body=post_body_str
    )

    endpoint = 'https://' + request_dict["host"] + request_dict["uri"]
    r = requests.post(endpoint, headers=request_dict["headers"], data=post_body_str)
    return r.status_code


def iot_get(aws_config):
    import awsiot_sign
    import trequests as requests
    request_dict = awsiot_sign.request_gen(aws_config['endpt_prefix'],
                                           thing_id(),
                                           aws_config['akey'],
                                           aws_config['skey'],
                                           get_date_time_stamp(),
                                           region=aws_config['region'])

    endpoint = 'https://' + request_dict["host"] + request_dict["uri"]
    try:
        r = requests.get(endpoint, headers=request_dict["headers"])
    except Exception as e:
        print("exception on GET request: {}".format(e))
    return r.json()


def get_config(filename):
    import json
    try:
        with open(filename) as f:
            config = json.load(f)
        return config
    except OSError as e:
        print("Error reading {}: {}".format(filename, str(e)))
        return None


def get_date_time_stamp():
    from ntptime import time as ntp_time
    import utime
    for _ in range(5):
        try:
            ntp_utc = utime.localtime(ntp_time())
            break
        except Exception as e:
            print("Error retrieving NTP: {}".format(str(e)))
        utime.sleep_ms(3000)
    datestamp = "{0}{1:02d}{2:02d}".format(ntp_utc[0], ntp_utc[1], ntp_utc[2])
    timestamp = "{0:02d}{1:02d}{2:02d}".format(ntp_utc[3], ntp_utc[4], ntp_utc[5])
    return datestamp + "T" + timestamp + "Z"


def thing_id(prefix='ESP-'):
    from machine import unique_id
    id_reversed = unique_id()
    id_binary = [id_reversed[n] for n in range(len(id_reversed) - 1, -1, -1)]
    my_id = prefix + "".join("{:02x}".format(x) for x in id_binary)
    return my_id


def do_connect():
    import network
    import time
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('scanning network...')
        sta_if.active(True)
        scanned = sta_if.scan()
        # load in network config
        wpa_config = get_config('/config/wpa.json')
        for i in scanned:
            if i[0].decode() in wpa_config:
                print("Trying [{}]...".format(i[0].decode()))
                sta_if.connect(i[0].decode(), wpa_config[i[0].decode()])
                n = 0
                while n < 10 and not sta_if.isconnected():
                    time.sleep(1)
                    n += 1
                if sta_if.isconnected():
                    break
    print('network config:', sta_if.ifconfig())

    ap_if = network.WLAN(network.AP_IF)
    if not ap_if.isconnected():
        print('disabling access point interface')
        ap_if.active(False)


def block_sizer(blocks, bites_per_block=4096, output_format="{:0.2f} {}"):
    bites = blocks * bites_per_block
    if bites <= 1024:
        return output_format.format(bites, "B")
    elif bites <= 1024 ** 2:
        return output_format.format(bites / 1024, "K")
    elif bites <= 1024 ** 3:
        return output_format.format(bites / (1024 ** 2), "M")
    elif bites <= 1024 ** 4:
        return output_format.format(bites / (1024 ** 3), "G")
    else:
        return output_format.format(bites / (1024 ** 4), "T")


def blink(count=1, delay=2):
    import machine
    import time
    led = machine.Pin(0, machine.Pin.OUT)
    for _ in range(count):
        led.on()
        time.sleep(delay)
        led.off()
