"""
Find common typos such as multiple spaces between words, accidentally accidentally repeated words, or multiple exclamation marks at the end of sentences. Those are annoying!!
"""

import re


def findCommonTypos(input_string):
    input_string = re.sub(r"\s+", r" ", input_string)
    input_string = re.sub(r"(\b\w+\b)(?:\s+\1\b)", r"\1", input_string)
    input_string = re.sub(r"\!+", r"!", input_string)
    return input_string


if __name__ == "__main__":
    text = """
Find common typos such as     multiple    spaces    between words, accidentally accidentally repeated words, or multiple exclamation marks (!!!) at the end of sentences. Those are annoying!!!!
"""
    print(findCommonTypos(text))
