import logging.config

from flask import Flask, request

from logger_setup import dict_config
app = Flask(__name__)

logging.config.dictConfig(dict_config)
logger = logging.getLogger("general_logger.consumer")


@app.route("/consumer", methods=['POST'])
def consumer():
    data = request.get_json()
    message = data["message"]
    logger.info(msg=message)
    return message



if __name__ == "__main__":
    app.run(debug=False)