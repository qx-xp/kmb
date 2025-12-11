#!/usr/local/bin/python3.14
#
# Update dictionary words using a manually reviewed word list
#
# The list contains a list of words that may be prefixed by:
#   '--' (no quote): remove the word from the dictionary
#   '++' (no quote): add the word to the dictionary
#   no prefix: do nothing,
#     word will neither be removed nor added to the dictionary

import re
import os
import sys
from dictionary.spelling_bee_dictionary_updater import SpellingBeeDictionaryUpdater

def main():
    word_file   = 'words_bee.txt'
    review_file = "bee-review.txt"

    dictionaryUpdater = SpellingBeeDictionaryUpdater(word_file)
    dictionaryUpdater.update_from(review_file)


if __name__ == "__main__":
    main()
