"""
Debugging Coin Toss
The following program is meant to be a simple coin toss guessing game. The player gets
two guesses (it’s an easy game). However, the program has several bugs in it. Run through
the program a few times to find the bugs that keep the program from working correctly.

```python
import random
guess = ''
while guess not in ('heads', 'tails'):
	print('Guess the coin toss! Enter heads or tails:')
	guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
	print('You got it!')
else:
	print('Nope! Guess again!')
	guesss = input()
if toss == guess:
	print('You got it!')
else:
	print('Nope. You are really bad at this game.')
```
"""

import logging
import random
from logging import debug

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s - %(message)s")
logging.disable()

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    debug(guess)
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
toss = {
    0: "tails",
    1: "heads"
}[toss]
debug(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
if toss == guess:
    print('You got it!')
else:
    print('Nope. You are really bad at this game.')
