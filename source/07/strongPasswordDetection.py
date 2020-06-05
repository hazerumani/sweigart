"""
# Strong Password Detection #

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
"""

import re


def stringPasswordDetection(pswd):
    PATTERNS = [ \
        r"[0-9]",
        r"[a-z]",
        r"[A-Z]"
    ]
    cnt = True
    for s in PATTERNS:
        cnt = cnt and re.search(s, pswd) is not None
    return bool(len(pswd) >= 8 and cnt)


if __name__ == "__main__":
    ps = "12FFFFFgFFFFFFFF"
    print(stringPasswordDetection(ps))
