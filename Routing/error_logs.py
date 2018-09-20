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
print('queue_name2: ', queue_name)

severity = "error"
channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key=severity
                   )
channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key="warning"
                   )

print(' [*] Waiting for error or warning logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(' [x] warning or error %r' % body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
