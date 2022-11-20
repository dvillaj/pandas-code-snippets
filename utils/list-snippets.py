import logging
import glob
from elyra_utils import *

included_tags = set(["Bash"])
#excluded_tags = set(["Base", "Bash", "Exploring Data", "Data Analyisis", "Data Cleaning"])
excluded_tags = None

conf_logging()
logger = logging.getLogger("app")

themes = set()
print(f"Snippet including {included_tags} and excluding {excluded_tags}:")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        themes.add(get_theme(dictionary))
        print(f" - {get_language(dictionary)}: {get_title(dictionary)} - {get_tags(dictionary)}")

print("\nThemes:")
for theme in sorted(themes):
    print(f"\t- {theme}")   

            



