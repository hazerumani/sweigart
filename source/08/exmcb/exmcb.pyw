"""
# Extending the Multiclipboard #

Extend the multiclipboard program in this chapter so that it has a `delete <keyword>` command line argument that will delete a keyword from the shelf. Then add a delete command line argument that will delete _all_ keywords.
"""

# ! python3
# exmcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe exmcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe exmcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe exmcb.pyw list - Loads all keywords to clipboard.
#        py.exe exmcb.pyw delete - Delets all keywords from clipboard.
#        py.exe exmcb.pyw delete <keyword> - Deletes keyword from clipboard.

import pyperclip
import shelve
import sys

mcbShelf = shelve.open('exmcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
# Delete keyword or all keywords:
if len(sys.argv) > 1 and sys.argv[1].lower() == 'delete':
    if len(sys.argv) == 3:
        deleteKey = sys.argv[3]
        del mcbShelf[deleteKey]
    else:
        mcbShelf.clear()

mcbShelf.close()
