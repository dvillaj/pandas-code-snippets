import logging
import glob
from elyra_utils import *

included_tags = set(["Read & Write"])
#excluded_tags = set(["Base", "Bash", "Exploring Data", "Read & Write", "Data Analyisis", "Data Cleaning"])
excluded_tags = set(["Extra"])

conf_logging()
logger = logging.getLogger("app")

logger.info("Beginning ...")
for file in glob.glob("*.json"):
    #backup_file(file)
    dictionary = read_file(file)
    # logger.info(f"Cleaning '{get_title(dictionary)} ...")
    delete_file(file)
    save_file(file, dictionary)

snippets = []
print(f"Snippet including {included_tags} and excluding {excluded_tags}:")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        tags = get_tags(dictionary)
        del dictionary['metadata']['display_name']
        dictionary['main_title'] = list(included_tags.intersection(tags))[0]
        dictionary['theme'] = get_theme(dictionary)
        print(f" - {get_language(dictionary)}: {get_title(dictionary)}")
        # execute_code(dictionary)
        snippets.append(dictionary)
      

write_to_notebook(snippets, "C:\\Develop\\Projects\\Practicas-Pandas\\notebooks\\Pandas Snippets Notebook.ipynb")
