"""
# Filling in the Gaps #

Write a program that finds all files with a given prefix, such as _spam001.txt_, _spam002.txt_, and so on, in a single folder and locates any gaps in the numbering (such as if there is a _spam001.txt_ and _spam003.txt_ but no _spam002.txt_). Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
"""

import logging
import os
import re
import sys
from logging import debug

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(asctime)s line %(lineno)s %(message)s"
)


# logging.disable()


def searchBoundaries(pathToWork):
    files = os.listdir(pathToWork)
    files[:] = [file for file in files if re.search(r'file(\d{3})\.txt', file)]
    serialNumbers = []
    for file in files:
        serialNum = re.search(r'file(\d{3}).txt', file).group(1)
        serialNumbers.append(serialNum)
    serialNumbers.sort()
    firstNumber = serialNumbers[0]
    lastNumber = serialNumbers[len(serialNumbers) - 1]
    logging.debug(lastNumber)
    return files, int(firstNumber), int(lastNumber)


def fillingTheGaps(pathToWork):
    allesGut = True
    files, firstNumber, lastNumber = searchBoundaries(pathToWork)
    y = 0
    for i in range(firstNumber, lastNumber + 1):
        currentFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i))
        if not os.path.exists(currentFile):
            allesGut = False
            while True:
                nextFile = os.path.join(pathToWork, 'file{0:0>3}.txt'.format(i + y))
                if os.path.exists(nextFile):
                    os.rename(nextFile, currentFile)
                    debug(os.path.basename(nextFile) + ' was renamed to ' + os.path.basename(currentFile))
                    break
                else:
                    if i + y < lastNumber:
                        debug('file{0:0>3}.txt is missing!'.format(i + y))
                        y += 1
                        debug(y)
                        continue
                    else:
                        debug('There are no files to rename anymore')
                        sys.exit()
        else:
            debug('file{0:0>3}.txt is here'.format(i))
        if allesGut:
            print("All files are there.")


def main():
    fillingTheGaps(".\\test")


if __name__ == '__main__':
    main()
