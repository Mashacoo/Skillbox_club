import logging.config

import pika, sys, os

from logger_setup import dict_config


logging.config.dictConfig(dict_config)
logger = logging.getLogger("general_logger.consumer")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test_rabbitmq')

    def callback(ch, method, properties, body):
        # print(f" [x] Received {body}")
        logger.info(msg=f"Message from RabbitMQ was proceeded: {body}")

    channel.basic_consume(queue='test_rabbitmq', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
