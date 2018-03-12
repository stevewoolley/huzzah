import os
stats = os.statvfs('/')
print("Used space:  {:>10} k".format(stats[3] * 1024))
print("Free space:  {:>10} k".format(stats[2] * 1024))
print("Total space: {:>10} k".format((stats[3] + stats[2]) * 1024))
