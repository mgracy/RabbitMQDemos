import time
import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()

channel.queue_declare(queue='testTaskWorker', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received 3 %r" % body)
    time.sleep(0.3)
    # ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue='testWorker', no_ack=True)

print(' [*] Waiting for messages. To exit precc CTRL+C')

channel.start_consuming()
