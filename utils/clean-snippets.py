import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

logger.info("Beginning ...")
for file in glob.glob("*.json"):
    #backup_file(file)
    dictionary = read_file(file)
    logger.info(f"Cleaning '{get_title(dictionary)} ...")
    delete_file(file)
    save_file(file, dictionary)

logger.info("All good :-)")
