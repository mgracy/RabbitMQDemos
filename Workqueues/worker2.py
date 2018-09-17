import time
import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='testWorker')


def callback(ch, method, properties, body):
    print(" [x] Received 2 %r" % body)
    time.sleep(1)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue='testWorker')

print(' [*] Waiting for messages. To exit precc CTRL+C')

channel.start_consuming()
