import os
from confluent_kafka import Producer
import time

# Get Kafka Server from Env
KAFKA_SERVER = os.getenv("BOOTSTRAP_SERVERS")

# Create Kafka Producer linked to the kafka server instance
# Kafka runs on server 9092 -> our env var should be =  'localhost:9092'
conf = {'bootstrap.servers': KAFKA_SERVER}
producer = Producer(conf)


# Delivery report callback function for stream logging
def delivery_report(err, msg):
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


# # Produce a message
# producer.produce('test_topic', key='key1',
#                  value='Hello Kafka!', callback=delivery_report)
# producer.produce('test_topic', key='key2',
#                  value='Hello Kafka 2!', callback=delivery_report)
# producer.produce('test_topic', key='key3',
#                  value='Hello Kafka 3!', callback=delivery_report)

# producer.flush()

# Produce messages
for i in range(20):
    message = f"Hello Kafka here is message #{i+1}"
    producer.produce("sample_kafka_topic",
                     key=str(i), value=message,
                     callback=delivery_report)
    print(f"Produced: {message}")
    time.sleep(15)
    producer.flush()

print("Producer finished relaying messages. Gracefully Exiting")
