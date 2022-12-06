import logging
import glob
from elyra_utils import *

tags_list = [["Base"], ["Read & Write"], ["Data Analysis"], ['Data Cleaning', 'Regex']]

conf_logging()
logger = logging.getLogger("app")

path = "C:/Develop/Projects/Practicas-Pandas/notebooks/Snippets/"
logger.info(f"Exporting Snippets to Google Colab [{path}] ...")
for tags in tags_list:
    file = f"{tags[0]} Snippets Notebook.ipynb"
    logger.debug(f"Exporting {tags[0]} to Google Colab: {file}")
    export_tag_to_google_colab(tags, f"{path}{file}") 