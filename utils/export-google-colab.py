import logging
import glob
from elyra_utils import *

notebooks = {
    'Base': ["Base"],
    'Read & Write' : ["Read & Write"], 
    'Data Analysis': ["Data Analysis"],
    'Data Cleaning': ['Data Cleaning']
}

notebooks = {
    'Pandas': ["Base", "Read & Write", 'Data Analysis', 'Data Cleaning']
}

conf_logging()
logger = logging.getLogger("app")

path = "C:/Develop/Projects/Practicas-Pandas/Snippets/"
for item in notebooks.keys():
    file = f"{item} Snippets Notebook.ipynb"
    logger.info(f"Exporting {item} to Google Colab: {file}")
    export_tag_to_google_colab(notebooks[item], f"{path}{file}") 


logger.info(f"Exported Snippets to Google Colab [{path}] ...")    