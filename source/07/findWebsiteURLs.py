"""
Find website URLs that begin with _http://_ or _https://_.
"""

import re


def findURL(input_string):
    pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    regURL = re.compile(pattern)
    return regURL.findall(input_string)


if __name__ == "__main__":
    url = '<a href="https://hello.world.py">Hello, World</a><br><a href=http://go.org>Let\'s go!..<a>'
    print(findURL(url))
