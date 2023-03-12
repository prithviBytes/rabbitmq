import pika
import time
import random

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# Declare a queue to send messages to
queue_name = 'letter_box'
channel.queue_declare(queue=queue_name)
message_id = 0

while True:
    # Define the message to send
    message = f'Sending MessageId: {message_id}'
    # Publish the message to the queue
    channel.basic_publish(
        exchange='',     
        routing_key=queue_name,
        body=message
    )
    time.sleep(random.randint(1,4))
    message_id += 1
# Close the connection to RabbitMQ
connection.close()