import pika
import time
import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()
 
channel.queue_declare(queue='testWorker')
 
def callback(ch, method, properties, body):
    print(" [x] Received 1 %r" % body)
 
channel.basic_consume(callback, queue='testWorker', no_ack=True)
 
print(' [*] Waiting for messages. To exit precc CTRL+C')
i = 5
while i > 0:
    print('Count down in worker1, ', i)
    time.sleep(1)
    i -= 1

channel.start_consuming()
