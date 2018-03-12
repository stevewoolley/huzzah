# Network connectivity
The ESP8266 family (generally) has wifi connectivity.

Once the unit has micropython installed, 
here is a function you can and put in your boot.py file to automatically connect to your WiFi network:

```python
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    ap_if = network.WLAN(network.AP_IF)
    if not ap_if.isconnected():    
        print('disabling access point interface')
        ap_if.active(False)
```
