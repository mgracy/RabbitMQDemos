import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
print('queue_name1: ', queue_name)

severity = "info"
channel.queue_bind(exchange='topic_logs',
                   queue=queue_name,
                   routing_key="*.orange.*"
                   )

print(' [*] Waiting for *.orange.* logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(' [x] orange %r' % body)


channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()
