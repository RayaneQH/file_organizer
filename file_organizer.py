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


def check_situation():
    # We will check if the directory is empty or if it is orgnized before we begin executing programm
    if not os.path.isdir(path):
        print(f"The directory {path} doesn't exist")
        quit()
    from helper_functions import isEmpty

    if not isEmpty(path):
        print(f"the directory {path} is not empty ")
        quit()


def check_if_file_or_folder():
    pass


def check_duplication():
    pass


def check_category_type():
    pass


def move_file():
    pass


def loop_in_directory():
    pass


def main():
    directory_path = input("Enter the directory path you wanna orgnize: ")
    check_existence()
    check_organized()
    loop_in_directory()
