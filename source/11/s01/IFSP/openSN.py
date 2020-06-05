"""
Open several social network sites that you regularly check.
"""

import webbrowser

links = [
    "vk.com/im",
    "mail.google.com/",
    "mail.yandex.ru",
    "stepik.org/",
    "www.citilink.ru",
]

for link in links:
    webbrowser.open(f"https://{link}")
