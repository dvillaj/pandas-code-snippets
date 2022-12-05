import logging
import glob
from elyra_utils import *
import pandas as pd

included_tags = set(["Base"])
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

main_tittle_ordered = ["Base"]
theme_ordered = ["Creating NumPy Arrays", 
                  "Reshaping a NumPy Array",
                  "Accessing to NumPy Arrays",
                  "Filtering NumPy Arrays",
                  "Statistical methods in NumPy",
                  "Values and Index of a Serie",
                  "Creating a Serie",
                  "Transforming a Serie into a Python list",
                  "Empty or Null Values on a Serie",
                  "Accessing to Series",
                  "Filtering Series",
                  "Statistical methods in Series",
                  "Statistical methods in Series Using NumPy",
                  "Operating with Series",
                  "Manipulating Strings on Series",
                  "Transforming Series",
                  "Values, Columns and Index of a Dataframe",
                  "Creating a Dataframe",
                  "Convert a Serie into a Dataframe",
                  "Shape of a Dataframe",
                  "Column Selection on a Dataframe",
                  "Multi Column Selection on a Dataframe",
                  "Rows Selection by position",
                  "Single Row Selection by position",
                  "Rows Selection by condition",
                  "Operating with Columns in a Dataframe"
                ]

snippets = []
print(f"Snippet including {included_tags} and excluding {excluded_tags}:")
for file in glob.glob("*.json"):
    dictionary = read_file(file)
    if check_tags(dictionary, included_tags, excluded_tags):
        tags = get_tags(dictionary)
        del dictionary['metadata']['display_name']
        dictionary['main_title'] = list(included_tags.intersection(tags))[0]
        dictionary['theme'] = get_theme(dictionary)
        # print(f" - {get_language(dictionary)}: {get_title(dictionary)} - {get_tags(dictionary)} : {get_theme(dictionary)}")
        execute_code(dictionary)
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

print(dataframe.filter(["main_title", "theme", "display_name"]))
write_to_notebook(dataframe, "C:\\Develop\\Projects\\Practicas-Pandas\\notebooks\\Pandas Snippets Notebook.ipynb")
