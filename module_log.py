import sched, time
from datetime import datetime
from pprint import pprint as print
import os

import logging
from logging.handlers import RotatingFileHandler
import sys

def get_log_formatter():
    # https://tutorialedge.net/python/python-logging-best-practices/
    log_formatter = logging.Formatter('%(asctime)s %(levelname)-8s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s')
    logFile = './log.log'
    my_handler = RotatingFileHandler(
        logFile, mode='a', maxBytes=5*1024*1024,
        backupCount=2, encoding=None, delay=0)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.INFO)
    app_log = logging.getLogger('root')
    app_log.setLevel(logging.INFO)
    app_log.addHandler(my_handler)
    return app_log


if __name__ == '__main__':
    pass
