import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

included_tags = set(["Data Analyisis"])
excluded_tags = set([])

print(f"Snippet including {included_tags} and excluding {excluded_tags}:")

tag = 'Data Analysis'
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        if add_tag(dictionary, tag):
            logger.info(f"Adding '{tag}' tag to {get_title(dictionary)} ...")
            delete_file(file)
            save_file(file, dictionary)


