# Practice Questions #

Q: 1. What is the difference between `shutil.copy()` and `shutil.copytree()`?

> The `shutil.copy()` function will copy a single file, while `shutil.copytree()` will copy an entire folder, along with all its contents.

Q: 2. What function is used to rename files?

> The `shutil.move()` function is used for renaming files, as well as moving them.

Q: 3. What is the difference between the delete functions in the `send2trash` and `shutil` modules?

> The `send2trash` functions will move a file or folder to the recycle bin, while `shutil` functions will permanently delete files and folders.

Q: 4. `ZipFile` objects have a `close()` method just like `File` objects’ `close()` method. What `ZipFile` method is equivalent to `File` objects’ `open()` method?

> The `zipfile.ZipFile()` function is equivalent to the `open() `function; the first
argument is the filename, and the second argument is the mode to open the ZIP file
in (read, write, or append).