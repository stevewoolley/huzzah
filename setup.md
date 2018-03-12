#Setup for ESP8266
Download latest/best version of the [micropython firmware](http://micropython.org/download#esp8266) for your ESP8266.
```bash
esptool.py --port /dev/tty.SLAB_USBtoUART write_flash -fm dio 0x00000 your_firmware_file.bin
```