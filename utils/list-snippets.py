import logging
import glob
from elyra_utils import *

included_tags = set(["Read & Write"]) #, "Base", "Read & Write", "Data Analysis", "Data Cleaning", "Regex"])
#included_tags = set(["Data Cleaning"])
#excluded_tags = set(["Base", "Read & Write", "Data Analysis", "Data Cleaning", "Regex"])
#excluded_tags = set(['Done'])
excluded_tags = None

conf_logging()
logger = logging.getLogger("app")

show_not_included = False
snippets_not_included = []
themes = set()
tags = set()
print(f"Snippet including {included_tags} and excluding {excluded_tags}:")
for file in glob.glob("*.json"):
    snippet = read_file(file)
    if check_tags(snippet, included_tags, excluded_tags):
        themes.add(get_theme(snippet))
        tags = tags.union(get_tags(snippet))
        extra = "*" if "Extra" in get_tags(snippet) else "-"
        done = "@" if "Done" in get_tags(snippet) else ""
        print(f" {extra}{done} {get_language(snippet)}: {get_title(snippet)} - {get_tags(snippet)}")
    else:
        snippets_not_included.append(snippet)

print("\nThemes:")
for theme in sorted(themes):
    print(f"- {theme}")   

print("\nTags:")
for tag in sorted(tags):
    print(f"- {tag}")   

if show_not_included:
    print("\nSnippets Not Included::")
    for snippet in snippets_not_included:
        print(f" - {get_language(snippet)}: {get_title(snippet)} - {get_tags(snippet)}")
            



