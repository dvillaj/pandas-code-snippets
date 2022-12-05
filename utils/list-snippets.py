import logging
import glob
from elyra_utils import *

included_tags = set(["Base", "Extra"])
#excluded_tags = set(["Base", "Bash", "Exploring Data", "Read & Write", "Data Analyisis", "Data Cleaning"])
excluded_tags = set([])

conf_logging()
logger = logging.getLogger("app")

show_not_included = False
snippets_not_included = []
themes = set()
tags = set()
print(f"Snippet including {included_tags} and excluding {excluded_tags}:")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        themes.add(get_theme(dictionary))
        tags = tags.union(get_tags(dictionary))
        print(f" - {get_language(dictionary)}: {get_title(dictionary)} - {get_tags(dictionary)}")
    else:
        snippets_not_included.append(dictionary)

print("\nThemes:")
for theme in sorted(themes):
    print(f"- {theme}")   

print("\nTags:")
for tag in sorted(tags):
    print(f"- {tag}")   

if show_not_included:
    print("\nSnippets Not Included::")
    for dictionary in snippets_not_included:
        print(f" - {get_language(dictionary)}: {get_title(dictionary)} - {get_tags(dictionary)}")
            



