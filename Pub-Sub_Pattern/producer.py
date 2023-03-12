import pika
from pika import exchange_type

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# The fanout exchange type is used in the Publish/Subscribe pattern to 
# distribute messages to all the queues that are bound to it. When a publisher 
# sends a message to a fanout exchange, the exchange forwards the message 
# to all the queues that are bound to it, regardless of the routing key or 
# message attributes.
exchange_name = "pubsub"
channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type.Fanout)

# Define the message to send
message = 'Broadcasting a message'
# Publish the message to the queue
channel.basic_publish(
    exchange=exchange_name,     
    body=message
)
# Close the connection to RabbitMQ
connection.close()