import logging
import glob
from elyra_utils import *

notebooks = {
    'Base': ["Base"],
    'Read & Write' : ["Read & Write"], 
    'Data Analysis': ["Data Analysis"],
    'Data Cleaning': ['Data Cleaning', 'Regex']
}

notebooks = {
    'Pandas': ["Base", "Read & Write", 'Data Analysis', 'Data Cleaning', 'Regex']
}

conf_logging()
logger = logging.getLogger("app")

path = "C:/Develop/Projects/Practicas-Pandas/notebooks/Snippets/"
logger.info(f"Exporting Snippets to Google Colab [{path}] ...")
for item in notebooks.keys():
    file = f"{item} Snippets Notebook.ipynb"
    logger.debug(f"Exporting {item} to Google Colab: {file}")
    export_tag_to_google_colab(notebooks[item], f"{path}{file}") 