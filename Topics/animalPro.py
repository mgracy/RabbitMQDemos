""" 
@author: glmgracy 
@file:   emit_log.py 
@time:   2018/09/17 下午10:51
"""

import ConnectionUtils
import time

connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')


message = "animal %s" % time.strftime('%Y-%m-%d %H:%M:%S')

channel.basic_publish(exchange='topic_logs',
                      routing_key=".orange.",
                      body=message)

print(' [x] Sent %r' % message)
connection.close()
