import logging
from common.tools import root_dir
import os
import datetime

now = datetime.datetime.now()
time = datetime.datetime.strftime(now, '%Y-%m-%d')

root = root_dir()
logs_path = os.path.join(root, 'logs')
if not os.path.exists(logs_path):
    os.mkdir(logs_path)
logfile_path = os.path.join(logs_path, f'api_{time}.log')


class Log:

    __logger = None

    def __new__(cls, *args, **kwargs):
        if cls.__logger is None:
            cls.__logger = logging.getLogger('cnodeApi')
            cls.__logger.setLevel(logging.DEBUG)

            fh = logging.FileHandler(logfile_path, encoding='utf-8')
            ch = logging.StreamHandler()

            formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            cls.__logger.addHandler(fh)
            cls.__logger.addHandler(ch)
        return cls.__logger


if __name__ == '__main__':
    log1 = Log()
    log2 = Log()
    log1.info("hello")


