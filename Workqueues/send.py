import pika
import time
import sys
import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()

channel.queue_declare(queue='testTaskWorker', durable=True)
i = 1
while i <= 50:
    message = ' '.join(sys.argv[1:]) or "Hello World Work queues!--%s" % int(i)
    channel.basic_publish(exchange='',
                          routing_key='testWorker',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                          ))
    print(" [x] Sending %r" % message)
    time.sleep(0.2)
    i += 1

connection.close();
