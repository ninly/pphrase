pphrase
=======

This script generates a 4-random-word passphrase (à la xkcd) using the 10,000
most common English words as determined by n-gram frequency analysis of
Google's Trillion Word Corpus (courtesy_ of `Josh Kaufman`_).

This was a morning-coffee project; just getting used to git submodules and the
github interface

.. _courtesy: https://github.com/first20hours/google-10000-english

.. _`Josh Kaufman`: http://first20hours.com/

Important!
----------

This has **no expectation or intention** of being cryptographically secure, or
a good idea to actually use in generating passphrases.

Usage
-----

It's easy::

    $ python pphrase.py
    correct horse battery staple

To do
-----

* Take command line arguments for passphrase length, or to use a custom word list.
