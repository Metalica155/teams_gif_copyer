#!/usr/bin/env python3

import argparse
import shutil
import os
import sys

TEAMS_FOLDER_PATH = "~/Library/Application Support/Microsoft/Teams/Backgrounds/Uploads/"

def remove_file_extension(file_name: str) -> str:
    return os.path.splitext(os.path.basename(file_name))[0]

    
def copy_file_to_teams_folder(source_file: str) -> None:
    file_names = create_teams_compatible_file_paths(source_file)

    if is_files_already_exists(file_names):
        sys.exit("Files are already exists")

    for file_name in file_names:
        shutil.copy(source_file, file_name)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("fileName")
    return parser.parse_args()


def is_files_already_exists(file_names: tuple) -> bool:
    for file_name in file_names: 
        if os.path.exists(file_name) == True:
            return True

    return False


def create_teams_compatible_file_paths(file_name: str) -> tuple:
    base_name = remove_file_extension(file_name)

    return (
        TEAMS_FOLDER_PATH + base_name + ".png",
        TEAMS_FOLDER_PATH + base_name + "_thumb.png"
    )


def main():
    args = parse_args()

    copy_file_to_teams_folder(args.fileName)


if __name__== "__main__":
    main()
    print("Success!")