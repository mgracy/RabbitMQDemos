"""
@ Author: glmgr
@ Email: 36040944@qq.com
@ Time: 2018/9/21 14:52
"""

import ConnectionUtils
import sys

connection = ConnectionUtils.connection
channel = connection.channel()
exchangeName = "testPersist"
queueName = "testPersistQueue"

channel.exchange_declare(exchange=exchangeName,
                         exchange_type='direct', durable=True)
channel.queue_declare(queue=queueName, durable=True)
channel.queue_bind(exchange=exchangeName, queue=queueName, routing_key="persist")


def callback(ch, method, properties, body):
    print('[x] receive %r' % body)


print('[x] receiving message...')
channel.basic_consume(callback, queue=queueName, no_ack=True)
channel.start_consuming()
