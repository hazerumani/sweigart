# http://requests.readthedocs.org/
# http://stackoverflow.com/a/1732454/1893164/
# https://nostarch.com/automatestuff/
import requests

res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
res.raise_for_status()
playFile = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    print(playFile.write(chunk))
playFile.close()
