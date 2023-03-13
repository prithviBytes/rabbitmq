import pika
from pika.exchange_type import ExchangeType

def on_request_message_received(ch, method, properties, body):
    print(f"Received request: {properties.correlation_id}")
    ch.basic_publish(
        "",
        routing_key=properties.reply_to,
        body=f"This is response to {properties.correlation_id}"
    )

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

request_queue_name = "request-queue"

channel.queue_declare(queue=request_queue_name)


channel.basic_consume(
    queue=request_queue_name,
    on_message_callback=on_request_message_received
)

print('Server Waiting for messages...')
channel.start_consuming()