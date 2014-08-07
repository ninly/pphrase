""" pphrase.py : Generate a random passphrase

    Generate a random passphrase from a subset of the most common
    words (max 10000) in Google's trillion-word corpus. See
    http://xkcd.com/936 for the motivation and inspiration.

    Licensed under terms of MIT license (see LICENSE-MIT)
    Copyright (c) 2014 Jason Conklin, <j@ninly.net>

Usage:
    pphrase.py [ -L | -R | -C | -T ] [ options ]

Options:
    -h, --help                      Show usage help (this screen).
    -v, --version                   Show version number and exit.
    -L, --normal                    Normal output (like this) [default].
    -R, --running                   Run output together (likethis).
    -C, --camelcase                 Output in CamelCase (LikeThis).
    -T, --titlecase                 Output in Title Case (Like This).
    -w N, --words=N                 Number of words in passphrase
                                    [default: 4].
    -m MAXWORD, --maxword=MAXWORD   Maximum word length, in characters
                                    [default: 10].
    -n MINWORD, --minword=MINWORD   Maximum word length, in characters
                                    [default: 2].
    -p POOL, --poolsize=POOL        Select from most common POOL words
                                    [default: 2048].
"""

import os
import random
from docopt import docopt

basedir = os.path.dirname(os.path.abspath(__file__))+'/'

if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.0.4')


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
        print('Could not even: {}'.format(e))
        return
    else:
        words = list(words)[:poolsize]

    return words


def get_mode():
    mode = str()
    if arguments['--running']:
        mode = 'running'
    elif arguments['--camelcase']:
        mode = 'camelcase'
    elif arguments['--titlecase']:
        mode = 'titlecase'
    else:
        mode = 'normal'
    return mode


def build_pph(numwords, mode='normal'):
    """Build the passphrase."""
    try:
        wordpool = get_pool()
        if not wordpool:
            raise ValueError('Could not generate specified word pool.')
        if len(wordpool) < numwords:
            raise ValueError('Word pool not large enough to generate '\
                            +'passphrase of specified length.')
    except ValueError as e:
        print('Could not even: {}'.format(e))
        return

    pph_words = list()
    pph_str = str()
    while len(pph_words) < numwords:
        next_word = random.choice(wordpool)
        if next_word not in pph_words:
            pph_words.append(next_word)

    if (mode == 'normal'):
        pph_str = ' '.join(pph_words)
    if (mode == 'running'):
        pph_str = ''.join(pph_words)
    if (mode == 'titlecase'):
        for i in xrange(numwords):
            pph_words[i] = pph_words[i].capitalize()
        pph_str = ' '.join(pph_words)
    if (mode == 'camelcase'):
        for i in xrange(numwords):
            pph_words[i] = pph_words[i].capitalize()
        pph_str = ''.join(pph_words)
    return pph_str



def main():
    """Output passphrase."""
    try:
        if sanitize_args(): raise ArgError
    except ArgError:
        return

    numwords = int(arguments['--words'])
    mode = get_mode()
    pph = build_pph(numwords, mode)
    if pph: print(pph)


if __name__ == "__main__":
    main()
