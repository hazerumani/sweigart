"""
# Regex Search #

Write a program that opens all _.txt_ files in a folder and searches for any line that matches a user-supplied regular expression. The results should be printed to the screen.
"""

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s — %(message)s")
import re
import glob


def regexSearch(search_text):
    # Step 1. Open all _.txt_ files in a folder.
    files = glob.glob("*txt")
    logging.debug(files)
    res = ""
    for file in files:
        with open(file, "r") as f:
            li = f.readlines()
        # Step 2. Searches for any line that matches a user-supplied regular expression.
        regString = re.compile(search_text)
        for row in li:
            logging.debug(regString.match(row) != None)
            if regString.match(row) != None:
                res += row
    # Step 3. Print to the screen.
    print(res)


if __name__ == '__main__':
    regexSearch("[H|h]")
