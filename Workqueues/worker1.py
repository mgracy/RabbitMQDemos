import time
import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()
 
channel.queue_declare(queue='testWorker')
 
def callback(ch, method, properties, body):
    print(" [x] Received 1 %r" % body)
 
channel.basic_consume(callback, queue='testWorker', no_ack=True)
 
print(' [*] Waiting for messages. To exit precc CTRL+C')

channel.start_consuming()
