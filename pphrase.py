"""
pphrase.py :

    Generate random passphrase from 10,000 most common words in Google N-grams
    (see http://xkcd.com/936).

    Licensed under terms of MIT license (see LICENSE-MIT)
    Copyright (c) 2014 Jason Conklin, <j@ninly.net>

Usage:
    pphrase.py [ options ]

Options:
    -h --help                       Show usage help (this screen).
    -v --version                    Show version number and exit.
    -w N --words=N                  Number of words in passphrase [default: 4].
    -m MAXWORD --maxword=MAXWORD    Maximum word length, in characters [default: 10].
    -n MINWORD --minword=MINWORD    Maximum word length, in characters [default: 2].
    -p POOL --poolsize=POOL         Select from most common POOL words [default: 10000].

"""

import random
import os
from docopt import docopt

basedir = os.path.dirname(os.path.abspath(__file__))+'/'

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.0.2')

def getwords(filename = basedir+'wordlist/google-10000-english.txt'):
    poolsize = int(arguments['--poolsize'])
    minword = int(arguments['--minword'])
    maxword = int(arguments['--maxword'])

    with open(filename,'r') as f:
        lines = list(f)[:poolsize]
    f.close()

    words = list()

    for line in lines:
        if len(line.strip()) >= minword and len(line.strip()) <= maxword:
            words.append(line.strip())

    return words

def main():
    numwords = int(arguments['--words'])
    # print(arguments)
    # numwords = 4
    words = getwords()
    for i in range(numwords):
        print random.choice(words),

if __name__ == "__main__":
    main()
