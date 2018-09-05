import logging


def get_logger(name):
    format_setting = '\t'.join([
        '%(asctime)s',
        'level:%(levelname)s',
        'file:%(filename)s',
        'line:%(lineno)d',
        'function:%(funcName)s',
        'message:%(message)s'
    ])
    date_format = 'time:[%Y/%m/%d %H:%M:%S]'
    formatter = logging.Formatter(fmt=format_setting,datefmt=date_format)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler('flask_debug.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    file_handler = logging.FileHandler('flask_info.log')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.propagate = False

    logger.info('lunch logger')

    return logger
