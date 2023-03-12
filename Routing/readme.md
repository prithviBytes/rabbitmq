# Routing

## Direct Exchange

In RabbitMQ, a Direct Exchange is a type of exchange that routes messages to queues based on a matching routing key. When a message is published to a Direct Exchange, the exchange uses the routing key of the message to determine which queues should receive the message.

Each queue that is bound to the Direct Exchange specifies a routing key, and the exchange forwards messages to the queues whose routing key matches the routing key of the message. Direct Exchanges are useful in scenarios where messages need to be selectively routed to specific queues based on their content.

To use a Direct Exchange in RabbitMQ, publishers specify a routing key when they publish a message to the exchange, and subscribers bind their queue to the exchange with a specific routing key. When a message is published to the exchange with a routing key, the exchange matches the routing key to the routing keys of the queues that are bound to the exchange and forwards the message to the appropriate queues.

Overall, a Direct Exchange in RabbitMQ is a powerful way to selectively route messages to specific queues based on their content, making it a valuable tool for building complex messaging systems.


## Topic Exchange

In RabbitMQ, a Topic Exchange is a type of exchange that routes messages to queues based on wildcard patterns of routing keys. When a message is published to a Topic Exchange, the exchange uses the routing key of the message and a matching pattern to determine which queues should receive the message.

Each queue that is bound to the Topic Exchange specifies a routing key pattern, which can include wildcards. The exchange forwards messages to the queues whose routing key pattern matches the routing key of the message. Topic Exchanges are useful in scenarios where messages need to be selectively routed to specific queues based on complex patterns of routing keys.

To use a Topic Exchange in RabbitMQ, publishers specify a routing key when they publish a message to the exchange, and subscribers bind their queue to the exchange with a specific routing key pattern. The routing key pattern can include one or more words, separated by dots, and can include two types of wildcards: * matches a single word, and # matches zero or more words.

When a message is published to the exchange with a routing key, the exchange matches the routing key to the routing key patterns of the queues that are bound to the exchange and forwards the message to the appropriate queues based on the matching patterns.

Overall, a Topic Exchange in RabbitMQ is a powerful way to selectively route messages to specific queues based on complex patterns of routing keys, making it a valuable tool for building flexible and scalable messaging systems.