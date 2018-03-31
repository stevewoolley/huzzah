import utils

aws_config = utils.get_config('/config/aws_info.json')
result = utils.iot_put(aws_config, {'foo': utils.get_date_time_stamp()})
print("status_code: {}".format(result.status_code))
