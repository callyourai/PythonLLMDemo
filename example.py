from confluent_kafka import Consumer, KafkaException, KafkaError

def create_consumer():
    # Configuration for Kafka Consumer with SASL authentication
    consumer_conf = {
        'bootstrap.servers': 'kafka-2.callyour.ai:9095',  # Replace with your Kafka broker
        'group.id': 'my_consumer_grouip',        # Consumer group ID
        'auto.offset.reset': 'earliest',        # Start reading at the beginning if no offset is present
        'sasl.mechanisms': 'PLAIN',             # SASL mechanism
        'security.protocol': 'SASL_PLAINTEXT',  # Security protocol
        'sasl.username': '<username>',       # Replace with your username
        'sasl.password': '<password>'        # Replace with your password
    }
    return Consumer(consumer_conf)

def consume_messages(consumer, topic):
    # Subscribe to the topic
    consumer.subscribe([topic])
    print(f"Consuming messages from topic: {topic}")

    try:
        while True:
            msg = consumer.poll(timeout=10.0)  # Poll for messages
            print(msg)

            if msg is None:
                print("No message received within timeout")
                continue  # No message received (timeout)

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    print(f"Reached end of partition: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                # Proper message received
                print(f"Received message: {msg.value().decode('utf-8')} from topic: {msg.topic()} partition: {msg.partition()} offset: {msg.offset()}")

    except KeyboardInterrupt:
        print("Consumer interrupted by user")

    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

if __name__ == "__main__":
    consumer = create_consumer()
    topic = "conversationTopic"  # Replace with your topic name
    consume_messages(consumer, topic)
