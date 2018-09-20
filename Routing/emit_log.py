""" 
@author: glmgracy 
@file:   emit_log.py 
@time:   2018/09/17 下午10:51
"""

import ConnectionUtils
import random

connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severities = ["info", "warning", "error"]
severity = random.choices(severities)[0]
print('severity: ', severity)

message = "log severity is %s" % severity

channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(' [x] Sent %r' % message)
connection.close()
