import os
import utils

stats = os.statvfs('/')
print("Used space:  {}".format(utils.block_sizer(stats[3])))
print("Free space:  {}".format(utils.block_sizer(stats[2])))
print("Total space: {}".format(utils.block_sizer(stats[3] + stats[2])))
