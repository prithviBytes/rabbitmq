import pika
from pika.exchange_type import ExchangeType

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# The fanout exchange type is used in the Publish/Subscribe pattern to 
# distribute messages to all the queues that are bound to it. When a publisher 
# sends a message to a fanout exchange, the exchange forwards the message 
# to all the queues that are bound to it, regardless of the routing key or 
# message attributes.
exchange_name = "pubsub"
channel.exchange_declare(exchange=exchange_name, exchange_type=ExchangeType.fanout)

# Define the message to send
message = 'Broadcasting a message'
# When a message is published to an exchange with an empty routing key, 
# the message is forwarded to all the queues that are bound to that exchange. 
# This is because the routing key is used by the exchange to determine which 
# queues should receive the message. When the routing key is empty, all queues 
# that are bound to the exchange will receive the message.
channel.basic_publish(
    exchange=exchange_name,
    routing_key='',
    body=message
)
# Close the connection to RabbitMQ
connection.close()