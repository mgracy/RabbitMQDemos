import time
import ConnectionUtils

connection = ConnectionUtils.connection
channel = connection.channel()
 
channel.queue_declare(queue='hello')
i = 1
while i < 10:
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!--%s' % int(i))
    print(" [x] Sending Hello world!--%s" % int(i))
    time.sleep(2)
    i += 1
 
connection.close()
