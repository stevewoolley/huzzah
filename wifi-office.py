def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('i3wpa', 'I3wPak3y')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if = network.WLAN(network.AP_IF)
    if not ap_if.isconnected():
        print('disabling access point interface')
        ap_if.active(False)


do_connect()
