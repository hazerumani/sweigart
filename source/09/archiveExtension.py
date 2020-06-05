import logging
import os
import zipfile
from logging import debug

logging.basicConfig(level=logging.DEBUG, format="%(message)s")


# 1. Walk a directory tree and archive just files with certain extensions, such as `.txt` or `.py`, and nothing else
def archive_extension(folder, *extensions):
    zipFilename = os.path.basename(folder) + ".zip"
    backupZip = zipfile.ZipFile(zipFilename, "w")
    for root, dirs, files in os.walk(folder):
        for file in files:
            for extension in extensions:
                if file.endswith(extension):
                    file = os.path.join(root, file)
                    backupZip.write(file)
    backupZip.close()


# 2. Walk a directory tree and archive every file except the `.txt` and `.py` ones
def archive_except_extension(folder, *extensions):
    zipFilename = "__" + os.path.basename(folder) + ".zip"
    backupZip = zipfile.ZipFile(zipFilename, "w")
    for root, dirs, files in os.walk(folder):
        for file in files:
            check = True
            for extension in extensions:
                if file.endswith(extension):
                    check = False
            if check == True:
                file = os.path.join(root, file)
                debug(file)
                backupZip.write(file)
    backupZip.close()


# 3. Find the folder in a directory tree that has the greatest number of files or the folder that uses the most disk space
def findf_wgn_of_files(folder):
    gr = greatest_number(folder)
    md = most_diskspace(folder)
    return (gr, md)


def greatest_number(folder):
    number_of_files = 0
    greatest_folder = ""
    for root, dirs, file in os.walk(folder):
        # exclude hidden folders
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        number_of_files_in_current_folder = len(os.listdir(root))
        if number_of_files_in_current_folder > number_of_files:
            number_of_files = number_of_files_in_current_folder
            greatest_folder = root
    debug((greatest_folder, number_of_files))
    return (greatest_folder, number_of_files)


def most_diskspace(folder):
    total_size = 0
    heaviest_folder = ""
    for root, dirs, files in os.walk(folder):
        total_size_current_root = 0
        # exclude hidden folders
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        files = [x for x in files if not x.startswith(".")]
        for file in files:
            total_size_current_root = os.path.getsize(os.path.join(root, file))
        if total_size_current_root > total_size:
            total_size = total_size_current_root
            heaviest_folder = root
    debug((heaviest_folder, total_size))
    return (heaviest_folder, total_size)


def main():
    archive_extension("automate_online-materials", ".txt", ".pdf")
    archive_except_extension("automate_online-materials", ".txt", ".pdf", ".py")
    findf_wgn_of_files("automate_online-materials")


if __name__ == '__main__':
    main()
