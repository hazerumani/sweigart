"""
# Image Site Downloader

Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
"""

import os
import re
import requests
import sys
from selenium import webdriver


def get_only_letters(str):
    return re.sub(r"https:\/\/i\.imgur\.com\/[^a-z]|\?maxwidth.+", "", str)


def main(argv):
    if len(argv) < 1:
        raise ValueError("The query must be at least one word.")

    url = "https://imgur.com/"

    folder = "imgur"
    os.makedirs(folder, exist_ok=True)

    browser = webdriver.Firefox()
    browser.get(url)
    search = browser.find_element_by_css_selector(".Searchbar-textInput")
    search.send_keys(argv)
    search.submit()
    browser.implicitly_wait(7)
    images = browser.find_elements_by_css_selector(".image-list-link > img")
    print(images)
    for image in images:
        image_url = image.get_attribute("src")
        print(image_url)
        res = requests.get(image_url)
        res.raise_for_status()
        filename = os.path.basename(get_only_letters(image_url))
        print(filename)
        with open(os.path.join(folder, filename), "wb") as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
    browser.close()


if __name__ == '__main__':
    main(sys.argv[1:])
