""" 
@author: glmgracy 
@file:   receive_logs.py 
@time:   2018/09/17 下午10:56
"""

import ConnectionUtils


connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='fanout_logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print('queue_name1: ', queue_name)

channel.queue_bind(exchange='fanout_logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(' [x] 1111 %r' % body)

channel.basic_consume(callback, queue=queue_name,no_ack=True)

channel.start_consuming()