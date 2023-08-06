import os
from os.path import isdir
import shutil as SH
import hashlib as hash
import re
import PIL

from helper_functions.isEmpty import isEmpty


wanna_suffixes: str | None = None
wanna_upper_or_lower: str | None = None
wanna_CSVfile_Excelfile: str | None = None


def check_situation(path):
    # We will check if the directory is empty or if it is orgnized before we begin executing programm
    if not os.path.isdir(path):
        print(f"The directory {path} doesn't exist")
        quit()
    from helper_functions import isEmpty
    situ, data, dir=isEmpty.isEmpty(path, "categoties_types.json")
    if situ=="empty":
        print(f"the directory {path} is not empty ")
        quit()
    elif situ=="organized":
        print(f"the directory {path} is alredy organized")
        quit()
    return data, dir

def check_if_file_or_folder(file):
    if os.path.isdir(file):
        

def check_duplication(file, set_of_files):
    if file not in set_of_files:
        


def check_category_type():
    pass


def move_file():
    pass


def loop_in_directory(dir):
    set_of_files = set()
    for file in dir:
        check_if_file_or_folder(file)
        check_duplication(file, set_of_files)
        check_category_type(file, data)
        move_file(file)

def main():
    directory_path = input("Enter the directory path you wanna orgnize: ")
    data, dir=check_situation(directory_path)
    loop_in_directory(dir)


if __name__ == "__main__":
    main()
