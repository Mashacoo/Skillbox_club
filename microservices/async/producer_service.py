import time
import requests
import logging.config
from logger_setup import dict_config
import pika



URL = 'https://techy-api.vercel.app/api/json'

logging.config.dictConfig(dict_config)
logger = logging.getLogger("general_logger.producer")


def producer(quantity: int):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='test_rabbitmq')

    for num in range(quantity):
        response = requests.get(URL).json()['message']
        channel.basic_publish(exchange='',
                              routing_key='test_rabbitmq',
                              body=response)
        time.sleep(0.2)
        logger.info(msg=f"{num + 1}: {response}")
    connection.close()


if __name__ == "__main__":
    producer(20)
