import network
import time


def wifi_connect(essid, password):
    # Connect to the wifi. Based on the example in the micropython
    # documentation.
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network {}...'.format(essid))
        wlan.connect(essid, password)
        # connect() appears to be async - waiting for it to complete
        while not wlan.isconnected():
            print('waiting for connection...')
            time.sleep(4)
            print('checking connection...')
        print('Wifi connect successful, network config: {}'.format(wlan.ifconfig()))
    else:
        # Note that connection info is stored in non-volatile memory. If
        # you are connected to the wrong network, do an explicity disconnect()
        # and then reconnect.
        print('Wifi already connected, network config: {}'.format(wlan.ifconfig()))


def wifi_disconnect():
    # Disconnect from the current network. You may have to
    # do this explicitly if you switch networks, as the params are stored
    # in non-volatile memory.
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print("Disconnecting...")
        wlan.disconnect()
    else:
        print("Wifi not connected.")


def disable_wifi_ap():
    # Disable the built-in access point.
    wlan = network.WLAN(network.AP_IF)
    wlan.active(False)
    print('Disabled access point, network status is {}'.format(wlan.status()))


if __name__ == "__main__":
    # initialize hardware
    wifi_connect('i3wpa', 'I3wPak3y')
    time.sleep(10)
    wifi_disconnect()
