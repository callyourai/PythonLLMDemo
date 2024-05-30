from confluent_kafka import Consumer, KafkaException, KafkaError
import json
import logging
import time
from models.ConversationPayload import ConversationPayload
import pdb

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_consumer():
    # Configuration for Kafka Consumer with SASL authentication
    consumer_conf = {
        'bootstrap.servers': 'kafka-2.callyour.ai:9095',
        'group.id': 'my_consumer_group',
        'auto.offset.reset': 'earliest',
        'sasl.mechanisms': 'PLAIN',
        'security.protocol': 'SASL_PLAINTEXT',
        'sasl.username': 'llmservice_user',
        'sasl.password': '22b389f67b25426775e74b2a00bcd91a',
        'session.timeout.ms': 60000,  # Increase session timeout to 60 seconds
        'heartbeat.interval.ms': 15000,  # Increase heartbeat interval to 15 seconds
        'max.poll.interval.ms': 300000  # Increase max poll interval to 300 seconds
    }
    return Consumer(consumer_conf)

def consume_messages(consumer, topic):
    consumer.subscribe([topic])
    logger.info(f"Consuming messages from topic: {topic}")

    while True:
        try:
            msg = consumer.poll(timeout=10.0)  # Poll for messages

            if msg is None:
                logger.info("No message received within timeout")
                continue  # No message received (timeout)

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    logger.info(f"Reached end of partition: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                else:
                    raise KafkaException(msg.error())
            else:
                # Proper message received
                msg_value = msg.value().decode('utf-8')

                try:
                    # Deserialize JSON message to ConversationPayloa
                    conversation_payload = ConversationPayload.model_validate_json(msg_value)
                    logger.info(f"Received conversation: {conversation_payload} from topic: {msg.topic()} partition: {msg.partition()} offset: {msg.offset()}")
                except Exception as e:
                    logger.error(f"Error deserializing message: {e}")
                    continue  # Skip this message and continue

                # Optionally use pdb to debug if needed
                pdb.set_trace()

        except KafkaException as e:
            logger.error(f"Kafka error: {e}")
            # Implementing retry logic with exponential backoff
            for attempt in range(1, 6):
                try:
                    logger.info(f"Attempt {attempt}: Retrying in {2 ** attempt} seconds...")
                    time.sleep(2 ** attempt)
                    consumer = create_consumer()  # Recreate consumer to reset connection
                    consumer.subscribe([topic])
                    break
                except Exception as retry_e:
                    logger.error(f"Retry {attempt} failed: {retry_e}")
        except Exception as e:
            logger.error(f"Error while consuming messages: {e}")
        finally:
            # Close down consumer to commit final offsets if needed.
            consumer.close()
            consumer = create_consumer()
            consumer.subscribe([topic])

if __name__ == "__main__":
    consumer = create_consumer()
    topic = "conversationTopic"
    consume_messages(consumer, topic)
