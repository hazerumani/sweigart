"""
# 2048 #

2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys. You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over and over again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, and left keystrokes to automatically play the game.
"""

from random import choice
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

keys = [
    Keys.ARROW_UP,
    Keys.ARROW_LEFT,
    Keys.ARROW_DOWN,
    Keys.ARROW_RIGHT,
]
browser = webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
htmlElem = browser.find_element_by_tag_name("html")
for i in range(100):
    htmlElem.send_keys(choice(keys))
browser.close()
