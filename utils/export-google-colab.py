import logging
import glob
from elyra_utils import *

tags = ["Base", "Read & Write", "Data Analysis"]

conf_logging()
logger = logging.getLogger("app")

path = "C:/Develop/Projects/Practicas-Pandas/notebooks/Snippets/"
logger.info(f"Exporting Snippets to Google Colab [{path}] ...")
for tag in tags:
    file = f"{tag} Snippets Notebook.ipynb"
    logger.info(f"Exporting {tag} to Google Colab: {file}")
    export_tag_to_google_colab(tag, f"{path}{file}") 