import pika
from pika.exchange_type import ExchangeType

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

exchange_name = "routing"
channel.exchange_declare(exchange=exchange_name, exchange_type=ExchangeType.direct)

# Define the message to send
message = 'Broadcasting a message'
channel.basic_publish(
    exchange=exchange_name,
    routing_key='paymentsonly',
    body=message
)
# Close the connection to RabbitMQ
connection.close()