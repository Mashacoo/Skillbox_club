import time
import requests
import logging.config
from logger_setup import dict_config

URL = 'https://techy-api.vercel.app/api/json'

logging.config.dictConfig(dict_config)
logger = logging.getLogger("general_logger.producer")


def producer(quantity: int, url_end_point: str):

    for num in range(quantity):
        response = requests.get(URL).json()
        requests.post(url=url_end_point, json=response)
        time.sleep(0.2)
        logger.info(msg=f"{num+1}: {response['message']}")


if __name__ == "__main__":
    producer(20, "http://127.0.0.1:5000/consumer")