import os
from confluent_kafka import Consumer, KafkaException, KafkaError
import time

# Get Kafka server from environment variable
KAFKA_SERVER = os.getenv('BOOTSTRAP_SERVERS')

# Kafka Consumer Configuration
conf = {
    'bootstrap.servers': KAFKA_SERVER,
    'group.id': 'kafka_sample_consumer_group',
    'auto.offset.reset': 'earliest',
    "enable.auto.commit": False
}

consumer = Consumer(conf)
consumer.subscribe(['sample_kafka_topic'])

# **Test Kafka Connection**
try:
    print(f"Testing connection to Kafka at {KAFKA_SERVER}...")
    metadata = consumer.list_topics(timeout=10)
    print(
        f"Connection successful! Found topics: {list(metadata.topics.keys())}")
except KafkaException as e:
    print(f"Failed to connect to Kafka: {e}")
    exit(1)

while 'sample_kafka_topic' not in list(metadata.topics.keys()):
    print("searching for topic .. ")
    time.sleep(7)

consumer.subscribe(['sample_kafka_topic'])
print(f"✅ Subscribed to topic: 'sample_kafka_topic'")
print(f"Listening for messages...")

time.sleep(15)

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    print(f"🔥 Message received: {msg.value().decode('utf-8')}")
