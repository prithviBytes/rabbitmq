import pika
import uuid

def on_reply_message_received(ch, method, properties, body):
    print("Reply received: ", body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

# Reply from the server will be sent to this queue and we shal consume it from the client
reply_queue = channel.queue_declare(queue='', exclusive=True)

# Client will consume messages from this queue
channel.basic_consume(
    queue=reply_queue.method.queue,
    auto_ack=True,
    on_message_callback=on_reply_message_received
)

message = "A message sent from Client"
request_queue_name = "request-queue"
channel.queue_declare(
    queue=request_queue_name
)

cor_id = str(uuid.uuid4())

print(f"Sending request: {cor_id}")

channel.basic_publish(
    exchange='',
    routing_key=request_queue_name,
    body=message,
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    )
)

print("Starting Client...")
channel.start_consuming()