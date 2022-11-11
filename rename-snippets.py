import logging
import json
import glob
import os
import shutil


def check_file_exists(file: str) -> bool:
    from os.path import exists

    return exists(file)


def conf_logging(config_file: str = 'logging.ini'):
    from logging.config import fileConfig

    if check_file_exists(config_file):
        fileConfig(config_file)

def read_file(file: str):
    try:
        logger.info(f"Processing '{file}' ...")
        with open(file, 'r') as json_data:
            json_data = json.load(json_data)
            return json_data

    except FileNotFoundError:
        logger.error(f"'{file}' not found.")

def dict_to_string(dictionary: dict) -> str:
    return json.dumps(dictionary, indent=3)

def get_hash(dictionary: dict):
    import hashlib

    value = dict_to_string(dictionary)
    hash_object = hashlib.md5(value.encode())
    return hash_object.hexdigest()

def save_file(filename: str, dictionary: dict):
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

def get_file_name(display_name: str, hash:str):
    import re
    return re.sub('[\W_]+', ' ', display_name) \
            .strip() \
            .lower() \
            .replace('  ', ' ') \
            .replace(' ','_') \
                + f"_{hash}.json"

conf_logging()
logger = logging.getLogger("app")

logger.info("Beginning ...")
for file in glob.glob("*.json"):
    #backup_file(file)
    dictionary = read_file(file)
    delete_file(file)
    save_file(file, dictionary)

logger.info("All good :-)")
