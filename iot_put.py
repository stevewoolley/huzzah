import awsiot_sign
import aws_thing
import trequests as requests
import utils
import ujson
import gc

aws_config = utils.get_config('aws_info.json')

post_body = {'state': {'reported': {}}}
post_body['state']['reported']['foo'] = aws_thing.get_date_time_stamp()
post_body_str = ujson.dumps(post_body)

request_dict = awsiot_sign.request_gen(
    aws_config['endpt_prefix'],
    aws_thing.thing_id(),
    aws_config['akey'],
    aws_config['skey'],
    aws_thing.get_date_time_stamp(),
    method='POST',
    region=aws_config['region'],
    body=post_body_str
)

gc.collect()

endpoint = 'https://' + request_dict["host"] + request_dict["uri"]
r = requests.post(endpoint, headers=request_dict["headers"], data=post_body_str)
print("status_code: {}".format(r.status_code))
