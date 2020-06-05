from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://inventwithpython.com")
linkElem = browser.find_element_by_link_text("YouTube")
print(type(linkElem))
linkElem.click()  # follows the "Read It Online" link
