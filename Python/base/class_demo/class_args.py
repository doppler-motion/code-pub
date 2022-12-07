import time

from loguru import logger


class CheckStrategy:
    def __init__(self, operation, **kwargs):
        self.operation = operation

        self.other_param = kwargs

    def output_result(self):
        if self.operation == 1:
            logger.info("do something")

        logger.info(self.other_param)


class ChildA:
    def __init__(self):
        self.params = []
        logger.info("ChildA init success!")

    def run(self):
        if not self.params:
            raise Exception("it is a empty list!")


if __name__ == "__main__":
    # 传字典
    test_dict = {"a": 1, "b": 2}
    check_cla = CheckStrategy(1, **test_dict)
    check_cla.output_result()
