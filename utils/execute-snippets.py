import logging
import glob
from elyra_utils import *

conf_logging()
logger = logging.getLogger("app")

erroneous_snippets = []
logger.info("Executing Snippets ...")
for file in glob.glob("*.json"):
    snippet = read_file(file)
    if not execute_snippet(snippet):
        erroneous_snippets.append(snippet)

logger.info("Erroneous Snippets ...")
for snippet in erroneous_snippets:
    print(f" - {get_language(snippet)}: {get_title(snippet)} - {get_tags(snippet)}")