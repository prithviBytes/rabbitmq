import pika
import time
import random

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# Declare a queue to send messages to
queue_name = 'letter_box'
channel.queue_declare(queue=queue_name)

# Define a callback function to process incoming messages
def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1,6)
    print(f"Message received: {body}, will take {processing_time} to complete")
    time.sleep(processing_time)
    # delivery_tag is a unique identifier for a message that RabbitMQ uses to keep 
    # track of which messages have been sent to which consumers. 
    # By specifying method.delivery_tag in ch.basic_ack(delivery_tag=method.delivery_tag), 
    # the consumer acknowledges the specific message that it has just processed.
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finshed Processing Message")

# prefetch_count=1 sets the maximum number of 
# unacknowledged messages that a consumer can receive at a time to 1.
channel.basic_qos(prefetch_count=1)

# Start consuming messages from the queue
channel.basic_consume(
    queue=queue_name,
    on_message_callback=on_message_received
)

print('Waiting for messages...')
channel.start_consuming()