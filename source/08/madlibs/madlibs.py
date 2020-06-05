"""
# Mad Libs #

Create a Mad Libs program that reads in text files and lets the user add their own text anywhere the word _ADJECTIVE_, _NOUN_, _ADVERB_, or _VERB_ appears in the text file. For example, a text file may look like this:

```
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
```

The program would find these occurrences and prompt the user to replace them.

```
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
```

The following text file would then be created:

```
The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.
```

The results should be printed to the screen and saved to a new text file.
"""

import logging
import re

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logging.disable()


def madlibs(filename, newfname="result.txt"):
    with open(filename, "r") as f:
        li = f.readlines()
    diGram = {
        "ADJECTIVE": "Enter an adjective: ",
        "NOUN": "Enter a noun: ",
        "VERB": "Enter a verb: "
    }
    logging.debug(diGram)
    res = ""
    for row in li:
        words = re.split(r"\W+", row)
        logging.debug(words)
        for word in words:
            if word in diGram:
                msg = diGram[word]
                logging.debug(msg)
                inp = input(msg)
                row = re.sub(word, inp, row, 1)
                logging.debug(row)
        res += "{}\n".format(row)
        logging.debug(res)
    with open(newfname, "w") as nf:
        nf.write(res)


if __name__ == '__main__':
    madlibs("test.txt")
