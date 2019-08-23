from flask import Flask, current_app
from api_v1 import api_bp_v1
import time
import logging


app = Flask(__name__)
app.register_blueprint(api_bp_v1)
# logging config
log_format = logging.Formatter(
    '[%(name)s]: [%(asctime)s] - [%(levelname)s] : %(message)s'
)
log_format.converter = time.gmtime
# mode = w: reset application.log every api initialization
file_handler = logging.FileHandler('application.log', mode='w')
file_handler.setFormatter(log_format)

logger = app.logger
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

if __name__ == "__main__":
    try:
        app.run(debug=False, host='0.0.0.0')
        logger.info("Server Started")
    except Exception as e:
        logger.exception(str(e))
