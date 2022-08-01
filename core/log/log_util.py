import logging
import logging.config
import os


class LogUtil(object):
    import logging

    log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
    logging.config.fileConfig(log_file_path)

    ERROR = logging.ERROR
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG

    @staticmethod
    def getLogger(name=None):
        logger = logging.getLogger(name)
        return logger