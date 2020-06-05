"""
# Regex Version of strip() #

Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

import re


def regstrip(s, args):
    if len(args) == 0:
        args = [" "]
    for arg in args:
        if arg == " ":
            arg = "\s"
        else:
            arg = "\\" + arg
    res = re.sub("^[{}]+|[{}]+$".format(args, args), "", s)
    return res


if __name__ == "__main__":
    s = "+++++++++++++++++ *****test* +  ++++++  ***  "
    delsyms = "+* "
    myans = regstrip(s, delsyms)
    pyans = s.strip(delsyms)
    print(myans)
    print(pyans)
    print(myans == pyans)
