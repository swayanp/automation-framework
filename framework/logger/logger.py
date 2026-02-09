from loguru import logger
import sys


def get_logger(log_level="INFO"):
    logger.remove()
    logger.add(
        sys.stdout,
        level=log_level,
        format="<green>{time}</green> | <level>{level}</level> | <level>{message}</level>"
    )
    return logger
