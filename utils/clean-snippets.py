import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

logger.info("Beginning ...")
for file in glob.glob("*.json"):
    try:
        snippet = read_file(file)
        logger.info(f"Cleaning '{get_title(snippet)} ...")    
        clean_snippet(file, snippet)
    except:
        raise Exception(f"Sorry, An exception occurred in file '{file}'")
    

logger.info("All good :-)")
