import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

included_tags = set(["Base"])
excluded_tags = None

print(f"Executing Snippets including {included_tags} and excluding {excluded_tags}:")

erroneous_snippets = []
for file in glob.glob("*.json"):
    snippet = read_file(file)
    if check_tags(snippet, included_tags, excluded_tags):
        if not execute_snippet(snippet):
            erroneous_snippets.append(snippet)

logger.info("Erroneous Snippets ...")
for snippet in erroneous_snippets:
    print(f" - {get_language(snippet)}: {get_title(snippet)} - {get_tags(snippet)}")