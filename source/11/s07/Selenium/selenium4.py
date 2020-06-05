from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://passport.yandex.ru/auth")
emailElem = browser.find_element_by_id("passp-field-login")
emailElem.send_keys("hazerumani")
emailElem.submit()
browser.implicitly_wait(5)
passwordElem = browser.find_element_by_id("passp-field-passwd")
passwordElem.send_keys("")
passwordElem.submit()
