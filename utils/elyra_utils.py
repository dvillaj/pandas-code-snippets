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
        logger.info(f"Reading '{file}' ...")
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
    file_name = get_file_name(dictionary["display_name"], get_hash(dictionary))
    logger.info(f"Writting '{file_name}' ...")

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
    
    snippet = dictionary['display_name']
    lines = dictionary['metadata']['code']
    language = dictionary['metadata']['language']

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