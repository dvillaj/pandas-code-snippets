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


def dict_to_string(dictionary: dict) -> str:
    return json.dumps(dictionary, indent=3)

def get_hash(dictionary: dict):
    import hashlib
    import re

    regex = r'[a-z]'
    value = dict_to_string(dictionary)
    hash_object = hashlib.md5(value.encode())
    return re.sub(regex, '', hash_object.hexdigest())


def save_file(filename: str, dictionary: dict):
    logger = logging.getLogger("utils")
    file_name = get_file_name(get_title(dictionary), get_hash(dictionary))
    logger.debug(f"Writing '{file_name}' ...")

    json_txt = dict_to_string(dictionary)
    f = open(file_name,"w")
    f.write(json_txt)
    f.close()


def delete_file(file_name: str):
    os.remove(file_name)


def backup_file(file_name: str):
    shutil.copyfile(file_name, file_name + ".bak")   


def get_file_name(display_name: str, hash:str, extension: str = 'json'):
    import re
    return re.sub('[\W_]+', ' ', display_name) \
            .strip() \
            .lower() \
            .replace('  ', ' ') \
            .replace(' ','_') \
                + f"_{hash}.{extension}"


def execute_code(dictionary: dict, file_name: str = 'snippet.py'):
    logger = logging.getLogger("utils")
    
    snippet = get_title(dictionary)
    lines = get_code(dictionary)
    language = get_language(dictionary)

    lines.insert(0, "from IPython.display import display")

    if language == "Python":
        logger.info(f"Executing '{snippet}' ...")

        with open(file_name, 'w') as fp:
            for item in lines:
                fp.write("%s\n" % item)

        return_value = os.system(f'python {file_name}')
        delete_file(file_name)

        for data_file in glob.glob("data.*"):
            delete_file(data_file)

        if return_value:
            logger.error(f"Sorry, There is an issue executing the snippet: {snippet}")
    else:
        logger.info(f"No Python Snippet. Can't be executed ...")


def add_tag(dictionary: dict, tag: str) -> None:
    tags = set(dictionary['metadata']['tags'])
    tags.add(tag)
    dictionary['metadata']['tags'] = list(tags)

def remove_tag(dictionary: dict, tag: str) -> None:
    tags = list(set(dictionary['metadata']['tags']))
    if tag in tags:
        tags.remove(tag)
        dictionary['metadata']['tags'] = list(tags)    

def get_code(dictionary: dict) -> list:
    return dictionary['metadata']['code']

def get_language(dictionary: dict) -> str:
    return dictionary['metadata']['language']

def get_tags(dictionary: dict) -> set:
    return set(dictionary['metadata']['tags'])

def get_title(dictionary: dict) -> str:
    return dictionary['display_name']
    

def get_theme(dictionary: dict):
    import re

    title = get_title(dictionary)
    regex = r'([^-]*)'
    return re.findall(regex, title)[0].strip()      

def check_lists_included_and(tags: list, included_tags:set = None ) -> bool:
    return included_tags.intersection(tags) == included_tags

def check_lists_included_or(tags: list, included_tags:set = None ) -> bool:
    for included_tag in included_tags:
            if included_tag in tags:
                return True
    return False

def check_lists_excluded(tags: list, excluded_tags:set = None ) -> bool:
    if excluded_tags:
        for excluded_tag in excluded_tags:
            if excluded_tag in tags:
                return False
    return True

def check_lists(tags: list, included_tags: set, excluded_tags:set = None ) -> bool:
    if check_lists_included_and(tags, included_tags):
        return check_lists_excluded(tags, excluded_tags)

def check_lists_or(tags: list, included_tags: set, excluded_tags:set = None ) -> bool:
    if check_lists_included_or(tags, included_tags):
        return check_lists_excluded(tags, excluded_tags)

def check_tags(dictionary: dict, included_tags: set, excluded_tags:set = None ) -> bool:
    return check_lists(get_tags(dictionary), included_tags, excluded_tags)

def check_tags_or(dictionary: dict, included_tags: set, excluded_tags:set = None ) -> bool:
    return check_lists_or(get_tags(dictionary), included_tags, excluded_tags)    

def generate_id() -> str:
    import uuid
    import random
    from datetime import datetime

    rnd = random.Random()
    random.seed(datetime.now().timestamp())
    return str(uuid.UUID(int=rnd.getrandbits(128), version=4))


def get_cells(snippets: list) -> list:
    n = 0
    cells = []
    for snippet in snippets:
        n += 2

        title = {
            "cell_type": "markdown",
            "id": generate_id(),
            "metadata": {},
            "source": [f"## {snippet['main_title']}: {get_title(snippet)}"]
            }

        lines = []
        for line in get_code(snippet):
            lines.append(f"{line}\n")

        code = {
        "cell_type": "code",
        "execution_count": n,
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
    notebook = get_notebook(randomize_list(snippets))
    json_object = json.dumps(notebook, indent=4)
    with open(filename, "w") as outfile:
        outfile.write(json_object)


def randomize_list(list: list) -> list:
    import random
    random.shuffle(list)

    return list