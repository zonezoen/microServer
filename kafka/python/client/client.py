from kafka import KafkaConsumer
import logging
logging.basicConfig(level=logging.DEBUG)
consumer = KafkaConsumer('test',
                         bootstrap_servers=['118.25.222.89:9092'],
                         api_version=(0, 10, 1)
                         )

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))
