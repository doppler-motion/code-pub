import logging
from random import randint

FMTDCIT = {
    "ERROR": "\033[31mERROR\033[0m",
    "INFO": "\033[37mINFO\033[0m",
    "DEBUG": "\033[1mDEBUG\033[0m",
    "WARN": "\033[33mWARN\033[0m",
    "WARNING": "\033[33mWARNING\033[0m",
    "CRITICAL": "\033[35mCRITICAL\033[0m",
}


class Filter(logging.Filter):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def filter(self, record: logging.LogRecord) -> bool:
        record.levelname = FMTDCIT.get(record.levelname)
        return True


filter = Filter()


# 测试修改上下文环境
class MyFilter(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        # 当有新日志需要被记录时，此函数会被调用，用于判断是否记录该日志
        # 返回True代表允许记录，False代表不允许记录。
        record.rand = randint(0, 1024)  # 此处修改上下文环境。
        return True


fmter = logging.Formatter("%(name)s - %(levelname)s - rand:%(rand)s - %(message)s")
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(fmter)
ch.addFilter(MyFilter())  # ch.addFilter(filter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

logger.info('test info')
logger.error('test error')
