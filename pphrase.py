"""
pphrase.py : generate 4-word random passphrase from 10,000 most common words in
Google N-grams, discounting words <= 2 letters long. 

TODO:
  * generate directly from google-10000-english file
  * allow for command-line argument to indicate phassphrase length in words

"""

import random

def getwords(filename = 'google-10000-english.txt'):
    with open(filename,'r') as f:
        lines = list(f)
    f.close()

    words = list()

    for line in lines:
        if len(line.strip()) > 2:
            words.append(line.strip())

    return words

def main(numwords = 4):
    words = getwords()
    for i in range(numwords):
        print random.choice(words),

if __name__ == "__main__":
    main()
