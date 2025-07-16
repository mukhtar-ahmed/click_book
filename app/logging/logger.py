import logging
import sys

logger = logging.getLogger("Click Book")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setFormatter(formatter)

logger.handlers = [stream_handler]

logger.info("Logging start")