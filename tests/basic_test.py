import time

from tests.utils import attach_logger
from loguru import logger

attach_logger(__file__, "tests")


def test_hello_world():
    logger.debug("hello world")
    time.sleep(1)

if __name__ == "__main__":
    test_hello_world()
    