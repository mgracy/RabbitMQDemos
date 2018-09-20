""" 
@author: glmgracy 
@file:   emit_log.py 
@time:   2018/09/17 下午10:51
"""

import ConnectionUtils
import sys

connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='fanout_logs',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

channel.basic_publish(exchange='fanout_logs',
                      routing_key='',
                      body=message)


print(' [x] Sent %r' % message)
connection.close()