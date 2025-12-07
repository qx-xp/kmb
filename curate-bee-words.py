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

def read_changes(file):
    change_matcher = re.compile(r'^(--|\+\+){1}(.+)$')

    words_to_add = set()
    words_to_remove = set()

    with open(file) as f:
        for line in f:
            word = line.strip().lower()
            match = change_matcher.match(word)
            if not match:
                continue

            if match.group(1) == '--': # remove
                words_to_remove.add(match.group(2))
                continue

            if match.group(1) == '++': # add
                words_to_add.add(match.group(2))
                continue

    return words_to_add, words_to_remove

def update_dictionary(source_file, words_to_add, words_to_remove):
    tmp_file = f"{source_file}.tmp"

    # curate the word list
    dictionary = set(words_to_add) # use a set to eliminate duplicates
    with open(source_file, 'r') as source:
        for line in source:
            word = line.strip().lower()

            # remove all words that are less than 4 letters
            if len(word) < 4:
                continue

            # remove words from the reviewed list
            if word in words_to_remove:
                continue

            dictionary.add(word)

    # output is a sorted unique list of words
    with open(tmp_file, "w") as out:
        for word in sorted(dictionary):
            out.write(f'{word}\n')

    try:
        os.rename(tmp_file, source_file)
    except FileNotFoundError:
        print(f"Error: '{tmp_file}' was not found.")
    except OSError as e:
        print(f"Error renaming {tmp_file} to {word_file}: {e}")


def main():
    word_file   = 'words_bee.txt'
    review_file = "bee-review.txt"

    words_to_add, words_to_remove = read_changes(review_file)
    update_dictionary(word_file, words_to_add, words_to_remove)


if __name__ == "__main__":
    main()
