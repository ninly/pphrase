"""
pphrase.py :

    Generate a random passphrase from the most common words (max 10000)
    in Google's trillion-word corpus. See http://xkcd.com/936 for the
    motivation and inspiration.

    Licensed under terms of MIT license (see LICENSE-MIT)
    Copyright (c) 2014 Jason Conklin, <j@ninly.net>

Usage:
    pphrase.py [ options ]

Options:
    -h --help                       Show usage help (this screen).
    -v --version                    Show version number and exit.
    -w N --words=N                  Number of words in passphrase
                                    [default: 4].
    -m MAXWORD --maxword=MAXWORD    Maximum word length, in characters
                                    [default: 10].
    -n MINWORD --minword=MINWORD    Maximum word length, in characters
                                    [default: 2].
    -p POOL --poolsize=POOL         Select from most common POOL words
                                    [default: 2048].

"""

import os
import random
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
