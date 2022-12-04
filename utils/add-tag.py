import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

new_tag = 'Extra'
logger.info("Beginning ...")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    logger.info(f"Adding '{new_tag}' tag to {get_title(dictionary)} ...")

    add_tag(dictionary, new_tag)
    delete_file(file)
    save_file(file, dictionary)

logger.info("All good :-)")
