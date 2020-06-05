"""
Clean up dates in different date formats (such as 3/14/2015, 03-14-2015, and 2015/3/14) by replacing them with dates in a single, standard format.
"""
# Standard date format: yyyy-mm-dd
#
import re


def cleanUp(input_string):
    PATTERNS = [
        (re.compile(r"(\d{1,2})[\/\.\-](\d{1,2})[\/\.\-](\d{4})"), "{2:4}-{0:0>2}-{1:0>2}"),
        (re.compile(r"(\d{4})[\.\\\/](\d{1,2})[\.\\\/](\d{1,2})"), "{0:4}-{1:0>2}-{2:0>2}")
    ]
    for pattern, formatter in PATTERNS:
        mo = pattern.search(input_string)
        while mo != None:
            text_for_replace = mo.group(0)
            print("text_for_replace is " + text_for_replace)
            text_for_formatting = mo.groups()
            print("text_for_formatting is " + "".join(text_for_formatting))
            input_string = input_string.replace(text_for_replace, formatter.format(*text_for_formatting))
            mo = pattern.search(input_string)
    return input_string


if __name__ == "__main__":
    text = """
Этот формат даты такой, какой должен быть: 2019-09-10.
Этот формат даты должен быть исправлен 1: 2019/09/10.
Этот формат даты должен быть исправлен 2: 2019.09.10.
Этот формат даты должен быть исправлен 3: 3/14/2015.
Этот формат даты должен быть исправлен 4: 03-14-2015.
Этот формат даты должен быть исправлен 5: 2015/3/14.
Этот формат даты должен быть исправлен 6: 3/14/2015.
Этот формат даты должен быть исправлен 7: 03.14.2015.
Этот формат даты должен быть исправлен 8: 2015.3.14.
Этот формат даты должен быть исправлен 9: 3.14.2015.
Этот формат даты должен быть исправлен 10: 3.14.2019.
Этот формат даты должен быть исправлен 11: 3/01/2019.
Этот формат даты должен быть исправлен 12: 3.1.2019.
"""
    print(cleanUp(text))
