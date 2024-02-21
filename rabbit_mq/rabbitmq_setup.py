import pika

# Setup RabbitMQ connection
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare a queue for processing quotes
channel.queue_declare(queue='pdf_process_queue')

# Close the connection
connection.close()
