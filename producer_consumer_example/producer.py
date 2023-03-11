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

# Define the message to send
message = 'Hello, RabbitMQ!'

# Publish the message to the queue
# ====================================================================================
# This section publishes the message to the queue. The basic_publish method 
# takes three arguments: the exchange name (an empty string means that we use 
# the default exchange), the routing key (which in this case is the name of the queue), 
# and the message body (which is the message we defined earlier).
# ====================================================================================
channel.basic_publish(
    exchange='',     
    routing_key=queue_name,
    body=message
)

# Close the connection to RabbitMQ
# ====================================================================================
# Finally, we close the connection to the RabbitMQ server. This is important to 
# do after we have finished using RabbitMQ, in order to release any resources 
# that were allocated.
# ====================================================================================
connection.close()