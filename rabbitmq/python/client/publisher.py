import pika

credentials = pika.PlainCredentials('zone', '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='118.25.222.89', port='5672', credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()