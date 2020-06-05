"""
>>> import webbrowser
>>> webbrowser.open('http://inventwithpython.com/')
"""

# ! python3
# mapIt.py — Launches a map in the browser using an address from the
# command line or clipboard.

import pyperclip
import sys
import webbrowser

if len(sys.argv) > 1:
    # Get address from command line.
    address = " ".join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open("http://www.google.com/maps/place/" + address)
