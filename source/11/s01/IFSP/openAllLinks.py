"""
Open all links on a page in separate browser tabs.
"""

import bs4
import logging
import requests
import webbrowser
from logging import debug

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s %(message)s"
)

response = requests.get("https://habr.com/ru/top/")
debug(response.text[0:20])
soup = bs4.BeautifulSoup(response.text)
for anchor in soup.find_all(lambda tag: tag.get("class") == ["post__title_link"]):
    webbrowser.open(anchor["href"])
