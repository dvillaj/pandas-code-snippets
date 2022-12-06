import logging
import glob
from elyra_utils import *

tags = ["Base", "Read & Write", ]

conf_logging()
logger = logging.getLogger("app")

logger.info("Cleaning Snippets ...")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    delete_file(file)
    save_file(file, dictionary)

path = "C:/Develop/Projects/Practicas-Pandas/notebooks/Snippets/"
for tag in tags:
    export_tag_to_google_colab(tag, f"{path}{tag} Snippets Notebook.ipynb") 