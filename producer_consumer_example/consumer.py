import pika

# Establish a connection to RabbitMQ server
# =============================================================================
# This line creates a connection to the RabbitMQ server running on the local 
# machine. The pika library provides the BlockingConnection class for synchronous 
# communication with RabbitMQ. The ConnectionParameters class is used to specify 
# the connection parameters, such as the hostname or IP address of the 
# RabbitMQ server.
# =============================================================================
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# Declare a queue to send messages to
# =============================================================================
# This section declares a queue named my_queue on the RabbitMQ server. The 
# queue_declare method is used to create or check the existence of a queue. 
# If the queue already exists, this method does nothing. If it doesn't exist, 
# the queue is created with the specified name.
# =============================================================================
queue_name = 'letter_box'
channel.queue_declare(queue=queue_name)

# Define a callback function to process incoming messages
# =============================================================================
# Here, we define a callback function that will be called each time a message 
# is received from the queue. The function takes four arguments: 
# ch (the channel object), method (a method frame that contains delivery information), 
# properties (message properties), and body (the message body).
# =============================================================================
def on_message_received(ch, method, properties, body):
    print(f"Message received: {body}")

# Start consuming messages from the queue
# =============================================================================
# Finally, we start consuming messages from the queue. The basic_consume method 
# takes three arguments: the queue name, the callback function to call when a 
# message is received, and auto_ack=True, which means that the message will be 
# automatically acknowledged when it is received.
# The start_consuming method is called to start the consuming process. 
# This method blocks the current thread and runs indefinitely until the program 
# is interrupted or an error occurs. Before starting to consume messages, 
# we print a message to indicate that we are waiting for messages.
# When a message is received, the callback function is called and the 
# message is processed. The auto_ack=True option means that the message 
# is automatically acknowledged when it is received, so we don't need to 
# manually acknowledge the message.
# =============================================================================

channel.basic_consume(
    queue=queue_name,
    auto_ack=True,
    on_message_callback=on_message_received
)

print('Waiting for messages...')
channel.start_consuming()