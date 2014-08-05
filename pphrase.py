""" pphrase.py : Generate a random passphrase

    Generate a random passphrase from a subset of the most common
    words (max 10000) in Google's trillion-word corpus. See
    http://xkcd.com/936 for the motivation and inspiration.

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
    arguments = docopt(__doc__, version='0.0.3')


class ArgError(Exception):
    """Error class with no ability to can."""
    def __init__(self, value="could not even."):
        self.value = value
    def __str__(self):
        return str(self.value)


def sanitize_args():
    """Check input args for sanity."""
    try:
        numwords = int(arguments['--words'])
        poolsize = int(arguments['--poolsize'])
        minword = int(arguments['--minword'])
        maxword = int(arguments['--maxword'])
    except ValueError:
        print("Error: Option arguments must be integers.")
        return 1

    try:
        if (minword < 1) or (maxword < 1) or (numwords < 1):
            raise ArgError("word count and length must be positive integers.")
        if (poolsize > 10000) or (poolsize < 1):
            raise ArgError("pool size must be between 1 and 10000.")
    except ArgError as e:
        print('Could not even: {}'.format(e))
        return 1

    return 0


def get_pool(filename = basedir+'wordlist/google-10000-english.txt'):
    """Generate word pool to user specifications."""
    poolsize = int(arguments['--poolsize'])
    minword = int(arguments['--minword'])
    maxword = int(arguments['--maxword'])
    with open(filename,'r') as f:
        lines = list(f)
    f.close()

    words = list()

    # cull outsized words
    for line in lines:
        if len(line.strip()) >= minword and len(line.strip()) <= maxword:
            words.append(line.strip())
    # only keep poolsize words
    try:
        if len(words) < poolsize:
            # words_avail = len(words)
            raise ArgError("only "+str(len(words))+" words in specified length range.")
    except ArgError as e:
        print('Could not even: {}'.format(e))
        return
    except:
        return
    else:
        words = list(words)[:poolsize]

    return words


def main():
    """Output passphrase."""
    try:
        if sanitize_args(): raise ArgError
    except ArgError:
        return

    numwords = int(arguments['--words'])
    wordpool = get_pool()
    if wordpool:
        for i in range(numwords):
            print random.choice(wordpool),


if __name__ == "__main__":
    main()
