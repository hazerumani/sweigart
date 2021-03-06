### Selenium’s `WebDriver` Methods for Finding Elements ###

| Method name                                                  | WebElement object/list returned                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `browser.find_element_by_class_name(name)`<br />`browser.find_elements_by_class_name(name)` | Elements that use the CSS class `name`                       |
| `browser.find_element_by_css_selector(selector)`<br/>`browser.find_elements_by_css_selector(selector)` | Elements that match the CSS `selector`                       |
| `browser.find_element_by_id(id)`<br/>`browser.find_elements_by_id(id)` | Elements with a matching `id` attribute value                |
| `browser.find_element_by_link_text(text)`<br/>`browser.find_elements_by_link_text(text)` | `<a>` elements that completely match the text provided       |
| `browser.find_element_by_partial_link_text(text)`<br/>`browser.find_elements_by_partial_link_text(text)` | `<a>` elements that contain the text provided                |
| `browser.find_element_by_name(name)`<br/>`browser.find_elements_by_name(name)` | Elements with a matching `name` attribute value              |
| `browser.find_element_by_tag_name(name)`<br/>`browser.find_elements_by_tag_name(name)` | Elements with a matching tag `name` (case insensitive; an `<a>` element is matched by `'a'` and `'A'`) |

### WebElement Attributes and Methods ###

| Attribute or method | Description |
| ------ | ---------- |
| `tag_name` | The tag name, such as `'a'` for an `<a>` element |
| `get_attribute(name)` | The value for the element’s `name `attribute |
| `text` | The text within the element, such as '`hello`' in `<span>hello</span>` |
| `clear()` | For text field or text area elements, clears the text typed into it |
| `is_displayed()` | Returns True if the element is visible; otherwise returns `False` |
| `is_enabled()` | For input elements, returns `True `if the element is enabled; otherwise returns `False` |
| `is_selected()` | For checkbox or radio button elements, returns `True `if the element is selected; otherwise returns `False` |
| `location` | A dictionary with keys `'x'` and `'y'` for the position of the element in the page |

### Commonly Used Variables in the `selenium.webdriver.common.keys` Module ###

| Attributes                                             | Meanings                                            |
| ------------------------------------------------------ | --------------------------------------------------- |
| `Keys.DOWN , Keys.UP , Keys.LEFT , Keys.RIGHT`         | The keyboard arrow keys                             |
| `Keys.ENTER , Keys.RETURN`                             | The `ENTER `and `RETURN` keys                       |
| `Keys.HOME , Keys.END , Keys.PAGE_DOWN , Keys.PAGE_UP` | The `home` , `end` , `pagedown `, and `pageup `keys |
| `Keys.ESCAPE , Keys.BACK_SPACE , Keys.DELETE`          | The `ESC` , `BACKSPACE `, and `DELETE` keys         |
| `Keys.F1 , Keys.F2 ,…, Keys.F12`                       | The `F1` to `F12` keys at the top of the keyboard   |
| `Keys.TAB`                                             | The `TAB `key                                       |

### Clicking Browser Buttons ###

`browser.back()`. Clicks the Back button.
`browser.forward()` Clicks the Forward button.
`browser.refresh()`. Clicks the Refresh/Reload button.
`browser.quit()`. Clicks the Close Window button.