import model_a
import model_b



import logging
import coloredlogs

fmt1 = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
fmt = "%(levelname)s [%(filename)s:%(lineno)d] %(message)s"
fmt = "[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s"
logging.basicConfig(format=fmt, level=logging.INFO)
# logging.root.setLevel(logging.INFO)
# coloredlogs.install(level="DEBUG", fmt=fmt)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logging.debug("00000000")
    logging.info("111111111")
    logging.error("222222222")
    logger.info("3333333333")
    model_a.func()
    model_b.func()