"""
# Selective Copy #

Write a program that walks through a folder tree and searches for files with a certain file extension (such as `.pdf` or `.jpg`). Copy these files from whatever location they are in to a new folder.
"""

import logging
import os
import shutil
from logging import debug

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")


def selectiveCopy(extension, path):
    # Step 0. Creates output folder
    output_folder = extension[1:].upper()
    debug(f"Output folder is {output_folder}")
    new_out_path = os.path.join(path, output_folder)
    if not os.path.exists(new_out_path):
        os.makedirs(new_out_path)
    debug(f"Output path is {new_out_path}")
    # Step 1. Walks through a folder tree
    for root, dirs, files in os.walk(path):
        # Step 2. Searches for files with a certain file extension
        for file in files:
            if file.endswith(extension):
                debug(file)
                filefullpath = os.path.join(root, file)
                debug(filefullpath)
                out_path = os.path.join(new_out_path, file)
                debug(out_path)
                # Step 3. Copies these files to current location with foldername "[EXTENSION]
                if not os.path.exists(out_path):
                    res = shutil.copy(filefullpath, new_out_path)
                    debug(res)


if __name__ == "__main__":
    selectiveCopy(".pdf", "C:\\Users\\050SHesteperovEK\\Desktop\\")
