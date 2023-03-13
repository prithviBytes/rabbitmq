import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"First_consumer has received the message")

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port=5672))
channel = connection.channel()

exchange_name = "pubsub"
channel.exchange_declare(exchange=exchange_name, exchange_type=ExchangeType.fanout)

current_queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(
    exchange=exchange_name, 
    queue=current_queue.method.queue
)

channel.basic_consume(
    queue=current_queue.method.queue,
    on_message_callback=on_message_received
)

print('Waiting for messages...')
channel.start_consuming()