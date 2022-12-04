import logging
import glob
from elyra_utils import *
import pandas as pd

included_tags = set(["Base"])
#excluded_tags = set(["Base", "Bash", "Exploring Data", "Read & Write", "Data Analyisis", "Data Cleaning"])
excluded_tags = set(["Extra"])

conf_logging()
logger = logging.getLogger("app")

main_tittle_ordered = ["Base"]
theme_ordered = ["Creating NumPy Arrays", "Maniputaling NumPy Arrays"]

snippets = []
print(f"Snippet including {included_tags} and excluding {excluded_tags}:")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        tags = get_tags(dictionary)
        print(f" - {get_language(dictionary)}: {get_title(dictionary)} - {get_tags(dictionary)}")
        del dictionary['metadata']['display_name']
        dictionary['main_title'] = list(included_tags.intersection(tags))[0]
        dictionary['theme'] = get_theme(dictionary)
        snippets.append(dictionary)

dataframe = (pd.json_normalize(snippets)
              .rename(columns = lambda column: column[9:] if column.startswith("metadata.") else column)
              .convert_dtypes()
              .assign(
                main_title = lambda dataset: pd.Categorical(dataset.main_title, categories=main_tittle_ordered, ordered=True),
                theme = lambda dataset: pd.Categorical(dataset.theme, categories=theme_ordered, ordered=True)
              )
              .sort_values(["main_title", "theme"], ascending = [True, True])
 )

dataframe.to_parquet("C:\\Develop\\Projects\\Practicas-Pandas\\notebooks\data\\snippets.parquet")

write_to_notebook(dataframe, "C:\\Develop\\Projects\\Practicas-Pandas\\notebooks\\Pandas Snippets Notebook.ipynb")