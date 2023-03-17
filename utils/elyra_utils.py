import logging
import json
import os
import shutil
import glob


def check_file_exists(file: str) -> bool:
    from os.path import exists

    return exists(file)


def conf_logging(config_file: str = 'utils/logging.ini'):
    from logging.config import fileConfig

    if check_file_exists(config_file):
        fileConfig(config_file)
    else:
        print("Do no exists!")

def read_file(file: str):
    logger = logging.getLogger("utils")
    try:
        logger.debug(f"Reading '{file}' ...")
        with open(file, 'r') as json_data:
            json_data = json.load(json_data)
            return json_data

    except FileNotFoundError:
        logger.error(f"'{file}' not found.")
        
    except:
        raise Exception(f"An exception occurred in file '{file}'")


def dict_to_string(snippet: dict) -> str:
    return json.dumps(snippet, indent=3)

def get_hash(snippet: dict):
    import hashlib
    import re

    regex = r'[a-z]'
    value = dict_to_string(snippet)
    hash_object = hashlib.md5(value.encode())
    return re.sub(regex, '', hash_object.hexdigest())


def save_file(filename: str, snippet: dict):
    logger = logging.getLogger("utils")
    file_name = get_file_name(get_title(snippet), get_hash(snippet))
    logger.debug(f"Writing '{file_name}' ...")

    json_txt = dict_to_string(snippet)
    f = open(file_name,"w")
    f.write(json_txt)
    f.close()


def delete_file(file_name: str):
    os.remove(file_name)


def backup_file(file_name: str):
    shutil.copyfile(file_name, file_name + ".bak")   

def clean_snippet(file_name: str, snippet: dict):
    delete_file(file_name)
    save_file(file_name, snippet)

def get_file_name(display_name: str, hash:str, extension: str = 'json'):
    import re
    return re.sub('[\W_]+', ' ', display_name) \
            .strip() \
            .lower() \
            .replace('  ', ' ') \
            .replace(' ','_') \
                + f"_{hash}.{extension}"

def execute_python_file(file_name: str) -> int:
    return os.system(f'python {file_name}')

def execute_snippet(snippet: dict, file_name: str = 'snippet.py'):
    logger = logging.getLogger("utils")
    
    title = get_title(snippet)
    lines = get_code(snippet)
    language = get_language(snippet)

    lines.insert(0, "from IPython.display import display")

    if language == "Python":
        logger.info(f"Executing '{title}' ...")

        with open(file_name, 'w') as fp:
            for item in lines:
                fp.write("%s\n" % item)

        return_value = execute_python_file(file_name)
        delete_file(file_name)

        for data_file in glob.glob("data.*"):
            delete_file(data_file)

        if return_value:
            logger.error(f"Sorry, There is an issue executing the snippet: {title}")
            return False
    else:
        logger.info(f"No Python Snippet. Can't be executed ...")

    return True


def add_tag(snippet: dict, tag: str) -> None:
    tags = set(snippet['metadata']['tags'])
    if not tag in tags:
        tags.add(tag)
        snippet['metadata']['tags'] = list(tags)
        return True
    
    return False

def remove_tag(snippet: dict, tag: str) -> None:
    tags = list(set(snippet['metadata']['tags']))
    if tag in tags:
        tags.remove(tag)
        snippet['metadata']['tags'] = list(tags) 
        return True

    return False   

def get_code(snippet: dict) -> list:
    return snippet['metadata']['code']

def get_language(snippet: dict) -> str:
    return snippet['metadata']['language']

def get_tags(snippet: dict) -> list:
    return snippet['metadata']['tags']

def get_title(snippet: dict) -> str:
    return snippet['display_name']
    

def get_theme(snippet: dict):
    import re

    title = get_title(snippet)
    regex = r'([^-]*)'
    return re.findall(regex, title)[0].strip()      

def check_lists_included_and(tags: list, included_tags:set = None ) -> bool:
    return included_tags.intersection(tags) == included_tags

def check_lists_included_or(tags: list, included_tags:set = None ) -> bool:
    if included_tags:
        for included_tag in included_tags:
                if included_tag in tags:
                    return True
    return False

def check_tags(snippet: dict, included_tags: set, excluded_tags:set = None ) -> bool:
    tags = set(get_tags(snippet))
    if check_lists_included_and(tags, included_tags):
        return not check_lists_included_or(tags, excluded_tags)

def generate_id() -> str:
    import uuid
    import random
    from datetime import datetime

    rnd = random.Random()
    random.seed(datetime.now().timestamp())
    return str(uuid.UUID(int=rnd.getrandbits(128), version=4))


def get_cells(snippets: list) -> list:
    cells = []
    for snippet in snippets:
        str_tag = f"{snippet['tag']}: " if  'tag' in snippet else ""

        title = {
            "cell_type": "markdown",
            "id": generate_id(),
            "metadata": {},
            "source": [f"## {str_tag}{get_title(snippet)}"]
            }

        lines = []
        for line in get_code(snippet):
            lines.append(f"{line}\n")

        code = {
        "cell_type": "code",
        "id": generate_id(),
        "metadata": {},
        "outputs": [],
        "source": lines
        }

        cells.append(title)
        cells.append(code)
    return cells


def get_notebook(snippets: list) -> dict:
    return {
            "cells": get_cells(snippets),
            "metadata": {
            "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
            },
            "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.9.5"
            }
            },
            "nbformat": 4,
            "nbformat_minor": 5
            }

def write_to_notebook(snippets: list, filename: str) -> None:
    logger = logging.getLogger("utils")

    logger.debug(f"Writting {filename} ...")
    notebook = get_notebook(randomize_list(snippets))
    json_object = json.dumps(notebook, indent=4)
    with open(filename, "w") as outfile:
        outfile.write(json_object)



def randomize_list(list: list) -> list:
    import random
    random.shuffle(list)

    return list

def get_snippets_by_tag(tag: str, excluded_tags: list = None) -> list:
    snippets = []
    for file in glob.glob("*.json"):
        snippet = read_file(file)
        if check_tags(snippet, set([tag]), set(excluded_tags)):
            snippet['tag'] = tag
            snippets.append(snippet)
            
    return snippets

def export_tag_to_google_colab(tags: list, fileName: str):
    logger = logging.getLogger("utils")

    snippets = []
    for tag in tags:
        for snippet in get_snippets_by_tag(tag, set(['Extra'])):
            logger.info(f" - {snippet['tag']}: {get_title(snippet)}")
            snippets.append(snippet)

    # Extra Snippet
    snippets.append({
        'tag': 'Google Colab',
        'display_name': "Code Snippets",
        'metadata': {
            'code': [
                "print(\"Hello Pandas ;-)\")"
              ]
        }
    })

    write_to_notebook(snippets, fileName)