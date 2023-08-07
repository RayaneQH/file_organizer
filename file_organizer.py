import os
from os.path import isdir
import shutil as SH
import hashlib as hash
import re
from sys import path
import PIL

import magic


wanna_suffixes: str | None = None
wanna_upper_or_lower: str | None = None
wanna_CSVfile_Excelfile: str | None = None


def check_situation(path):
    # We will check if the directory is empty or if it is orgnized before we begin executing programm
    if not os.path.isdir(path):
        print(f"The directory {path} doesn't exist")
        quit()

    from helper_functions.isEmpty import isEmpty

    categories_types_path = os.path.abspath("categories_types.json")
    situ, data, dir = isEmpty(path, categories_types_path)
    if situ == "empty":
        print(f"the directory {path} is not empty ")
        quit()
    elif situ == "organized":
        print(f"the directory {path} is alredy organized")
        quit()
    return data, dir


def check_if_file_or_folder(file, data):
    if os.path.isdir(file):
        path = os.getcwd(file)
        loop_in_directory(path, data)


def check_category_type(file, data):
    category, type_ = magic.from_file(file, mime=True).split("/")
    if not os.path.isdir(category):
        os.mkdir(category)
    path = os.getcwd(category)
    if not os.path.isdir(type_):
        os.mkdir(path)


def move_file(file):
    pass


def loop_in_directory(path, data):
    from helper_functions import find_deal_duplicate_files

    set_of_files = find_deal_duplicate_files.duplicate(path)
    for file in set_of_files:
        check_if_file_or_folder(file, data)
        check_category_type(file, data)
        move_file(file)


def main():
    directory_path = input("Enter the directory path you wanna orgnize: ")
    data, dir = check_situation(directory_path)
    loop_in_directory(directory_path, data)


if __name__ == "__main__":
    main()
