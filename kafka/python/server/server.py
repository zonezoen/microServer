from kafka import KafkaProducer
import logging
logging.basicConfig(level=logging.DEBUG)
producer = KafkaProducer(bootstrap_servers=['118.25.222.89:9092'],
                         api_version=(0, 10, 1)
                         )  # 此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]

for i in range(3):
    msg = "msg%d" % i
    producer.send('test', msg)
producer.close()
