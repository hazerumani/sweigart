import bs4

exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elements = exampleSoup.select("#author")
print(type(elements))
print(len(elements))
print(type(elements[0]))
print(elements[0].getText())
print(str(elements[0]))
print(elements[0].attrs)

print("=" * 10)

parapraphsElems = exampleSoup.select("p")
print(str(parapraphsElems[0]))
print(parapraphsElems[0].getText())

print(str(parapraphsElems[1]))
print(parapraphsElems[1].getText())

print(str(parapraphsElems[2]))
print(parapraphsElems[2].getText())

print("=" * 10)

spanElem = exampleSoup.select("span")[0]
print(str(spanElem))

print(spanElem.get("id"))
print(spanElem.get("some_nonexistent_addr") is None)
print(spanElem.attrs)
