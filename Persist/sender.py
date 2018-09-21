"""
@ Author: glmgr
@ Email: 36040944@qq.com
@ Time: 2018/9/21 14:32
"""
import pika
import ConnectionUtils
import time

connection = ConnectionUtils.connection
channel = connection.channel()
exchangeName = "testPersist"
channel.exchange_declare(exchange=exchangeName, exchange_type='direct', durable=True)
message = "persist %s" % time.strftime('%Y-%m-%d %H:%M:%S')
channel.basic_publish(exchange=exchangeName,
                      routing_key='persist',
                      body=message,
                      properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                      ))

print('[v] Sending %r' % message)
channel.close()
connection.close()


