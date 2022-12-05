import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

included_tags = set(["Read & Write"])
excluded_tags = set([])

print(f"Snippet including {included_tags} and excluding {excluded_tags}:")

tag = 'Extra'
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        logger.info(f"Removing '{tag}' tag from {get_title(dictionary)} ...")

        remove_tag(dictionary, tag)
        delete_file(file)
        save_file(file, dictionary)

logger.info("All good :-)")
