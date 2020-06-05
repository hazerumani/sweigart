# lucky.py — Opens several Google search results.
import logging
import sys
import webbrowser

from googlesearch import search

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(message)s"
)

print("Googling...")  # display text while downloading the Google page

query = " ".join(sys.argv[1::])
# Open a browser tab for each result.
for found in search(query, tld="co.in", num=10, stop=10, pause=2):
    webbrowser.open(found)
