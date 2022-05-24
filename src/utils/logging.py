import logging

logging.basicConfig(
    filename='./src/utils/savebread.log',
    level=logging.DEBUG,
    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
)


def get_logger(name=None):
    return logging.getLogger(name)
