import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

included_tags = set(["Base"])
excluded_tags = set(["NumPy"])

print(f"Snippet including {included_tags} and excluding {excluded_tags}:")

tag = 'Pandas'
for file in glob.glob("*.json"):
    snippet = read_file(file)
    if check_tags(snippet, included_tags, excluded_tags):
        if add_tag(snippet, tag):
            logger.info(f"Adding '{tag}' tag to {get_title(snippet)} ...")
            clean_snippet(file, snippet)


