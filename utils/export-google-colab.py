import logging
import glob
from elyra_utils import *

tags = ["Base", "Read & Write", ]

conf_logging()
logger = logging.getLogger("app")

path = "C:/Develop/Projects/Practicas-Pandas/notebooks/Snippets/"
for tag in tags:
    export_tag_to_google_colab(tag, f"{path}{tag} Snippets Notebook.ipynb") 