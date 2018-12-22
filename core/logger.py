import logging

class Logger(object):
    def __init__(self):
        logger = logging.getLogger('main')
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    @staticmethod
    def log_debug(msg):
        logger = logging.getLogger('main')
        logger.debug(msg)

    @staticmethod
    def log_info(msg):
        logger = logging.getLogger('main')
        logger.info(msg)

    @staticmethod
    def log_warn(msg):
        logger = logging.getLogger('main')
        logger.warn(msg)

    @staticmethod
    def log_error(msg):
        logger = logging.getLogger('main')
        logger.error(msg)

    @staticmethod
    def log_critical(msg):
        logger = logging.getLogger('main')
        logger.critical(msg)