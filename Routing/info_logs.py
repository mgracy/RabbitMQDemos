""" 
@author: glmgracy 
@file:   receive_logs.py 
@time:   2018/09/17 下午10:56
"""

import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print('queue_name1: ', queue_name)

severity = "info"
channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key=severity
                   )

print(' [*] Waiting for info logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(' [x] 1111 %r' % body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
