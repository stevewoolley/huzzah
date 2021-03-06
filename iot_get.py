import awsiot_sign
import trequests as requests
import utils
import gc

aws_config = utils.get_config('/config/aws_info.json')

request_dict = awsiot_sign.request_gen(aws_config['endpt_prefix'],
                                       utils.thing_id(),
                                       aws_config['akey'],
                                       aws_config['skey'],
                                       utils.get_date_time_stamp(),
                                       region=aws_config['region'])
gc.collect()

endpoint = 'https://' + request_dict["host"] + request_dict["uri"]
try:
    r = requests.get(endpoint, headers=request_dict["headers"])
except Exception as e:
    exception_msg = "Exception on GET request: {}".format(e)
print("r.status_code: {}".format(r.status_code))
print("result: {}".format(r.json()))
