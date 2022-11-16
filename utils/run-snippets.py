import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

logger.info("Beginning ...")
for file in glob.glob("data*.json"):
    dictionary = read_file(file)
    execute_code(dictionary)
