""" 
@author: glmgracy 
@file:   emit_log.py 
@time:   2018/09/17 下午10:51
"""

import ConnectionUtils
import random

connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')


message = "animal"

channel.basic_publish(exchange='topic_logs',
                      routing_key="quick.orange.rabbit",
                      body=message)

print(' [x] Sent %r' % message)
connection.close()
