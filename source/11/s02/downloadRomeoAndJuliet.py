import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
print(type(res))  # <class 'requests.models.Response'>
print(res.status_code == requests.codes.ok)  # True
print(len(res.text))  # 178981
print(res.text[:250:])
"""
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Proje
"""
