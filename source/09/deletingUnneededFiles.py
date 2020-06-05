"""
# Deleting Unneeded Files #

It's not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you're trying to free up room on your computer, you'll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders — say, ones that have a file size of more than 100MB. (Remember, to get a file's size, you can use `os.path.getsize()` from the `os` module.) Print these files with their absolute path to the screen.
"""

import logging
import os
from logging import debug

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s — %(message)s"
)


def findingUnneededFiles(folder):
    LARGE_SIZE = 100
    debug(LARGE_SIZE)
    fi_li = []
    # Walks through a folder tree
    for root, dirs, files in os.walk(folder):
        # Searches for exceptionally large files or folders
        for file in files:
            file_absolute_path = os.path.join(root, file)
            size = os.path.getsize(file_absolute_path) / 1024 / 1024
            # Print these files with their absolute path to the screen
            if size >= LARGE_SIZE:
                debug(f"{file_absolute_path} {size} MB")
                fi_li.append(file_absolute_path)
    return fi_li


def deletingAllFindedFiles(files):
    for file in files:
        debug(file)
        os.remove(file)


def deletingUnnededFiles(folder):
    findedFiles = findingUnneededFiles(folder)
    msg = "Delete current file ([Y]es/[N]o/[A]ll,[Q]uit)? >> "
    quit = False
    remainingFiles = findedFiles[:]
    for file in findedFiles:
        if quit == True:
            break
        ans = ""
        while ans != "y" and ans != "n" and ans != "a" and ans != "q":
            print(file)
            ans = input(msg).lower()
            debug(ans)
            if ans == "y":
                os.remove(file)
                print(f"Removing file \"{file}\"")
                remainingFiles.pop(0)
                debug(remainingFiles)
            elif ans == "a":
                deletingAllFindedFiles(remainingFiles)
            elif ans == "q":
                quit = True
                print("Quitting...")
                break
            elif ans == "n":
                break
    return True


def main():
    folder_name = "D:\\"
    print(deletingUnnededFiles(folder_name))


if __name__ == "__main__":
    main()
