import os
import re
import pandas as pd
from typing import List, Tuple, BinaryIO

current = os.getcwd()
files = os.listdir(path=current)
file_name = os.path.join(current, "docker_kubernetes.txt")
print(file_name)


def get_file_names() -> List[str]:
    new_file_names = []
    with open(file_name, "r") as f:
        file_names = f.readlines()
        i = 1
        for name in file_names:
            stripped_name = name.strip("\n")
            new_file_names.append(f"{i}. {stripped_name}")
            i += 1
    return new_file_names


def rename_file_names(files: BinaryIO, file_names: List):
    # i = 0

    for file in files:
        if file.endswith(".mp4"):
            n_file = file.strip("lesson").split(".mp4")[0]
            for file_name in file_names:
                match = re.search(r"\d+", file_name)
                number = match.group()
                if n_file == number:
                    print(number, n_file)
                    try:
                        os.rename(os.path.join(current, file), file_name + ".mp4")
                    except Exception as e:
                        print(e)


if __name__ == "__main__":
    file_names = get_file_names()
    rename_file_names(file_names=file_names, files=files)
    print()
