import re
import os


def check_valid_file_name(name):
    if len(name) == 0 or re.search(r'[\\/:*?"<>|]', name) or name[-1] == ".":
        return False
    return True


def construct_file_name(original_name):
    # File name collision resolution
    new_name = original_name
    counter = 1
    while os.path.isfile(new_name):
        new_name = f"{original_name} ({counter})"
        counter += 1
    # Ensures .txt extension
    if len(new_name) < 4 or not new_name[-4:] == ".txt":
        new_name += ".txt"
    return new_name