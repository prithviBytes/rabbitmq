import pika
from pika.exchange_type import ExchangeType

# Define a callback function to process incoming messages
def on_message_received(ch, method, properties, body):
    print(f"Payment Consumer has received a message")

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# Declaring an exchange from where we are supposed to receive the messages
exchange_name = "routing"
channel.exchange_declare(exchange=exchange_name, exchange_type=ExchangeType.direct)

current_queue = channel.queue_declare(queue='', exclusive=True)

# the subscriber ensures that it will receive messages that are published to that exchange.
channel.queue_bind(
    exchange=exchange_name, 
    queue=current_queue.method.queue,
    # !!!!!!!!!!!!!
    routing_key='paymentsonly'
)


# Start consuming messages from the queue
channel.basic_consume(
    queue=current_queue.method.queue,
    on_message_callback=on_message_received
)

print('Waiting for messages...')
channel.start_consuming()