import pika

def callback(ch, method, properties, body):
    print(f"Received {body}")
    # Here you would call the PDF creation logic

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='quote_queue')

channel.basic_consume(queue='quote_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
