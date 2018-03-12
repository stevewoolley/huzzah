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


def thing_id():
    from machine import unique_id
    id_reversed = unique_id()
    id_binary = [id_reversed[n] for n in range(len(id_reversed) - 1, -1, -1)]
    my_id = "ESP-" + "".join("{:02x}".format(x) for x in id_binary)
    return my_id
