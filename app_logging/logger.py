import logging
import logging.handlers
import time


log_file = 'Api.log'
logging.basicConfig(
    filename=log_file,
    filemode='w',
    format='[%(name)s]: [%(asctime)s] - [%(levelname)s] : %(message)s', level=logging.DEBUG
)
logging.Formatter.converter = time.gmtime
handler = logging.handlers.RotatingFileHandler(
              log_file, maxBytes=1000000, backupCount=1)

logger = logging.getLogger('ApiLog')
logger.addHandler(handler)

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too2')
