import re
from .dictionary_updater import DictionaryUpdater

class SpellingBeeDictionaryUpdater(DictionaryUpdater):
    default_wordfile = "words_bee.txt"

    def __init__(self, wordfile=default_wordfile):
        super().__init__(wordfile)

    def is_exclude_word(self, word):
        # remove all words that are less than 4 letters
        if len(word) < 4:
            return True

        # spelling bee only uses 7 unique characters
        if len(set(word)) > 7:
            return True

        return False

    # The file contains a list of words that may be prefixed by:
    #   '--' (no quote): remove the word from the dictionary
    #   '++' (no quote): add the word to the dictionary
    #   no prefix: do nothing to the word
    def load_changes(self, file):
        change_matcher = re.compile(r'^(--|\+\+)\s*(\w+)\s*$')

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
                    # do not add if the word is excluded
                    if self.is_exclude_word(match.group(2)):
                        continue

                    words_to_add.add(match.group(2))
                    continue

        return words_to_add, words_to_remove

    def update_from(self, file):
        words_to_add, words_to_remove = self.load_changes(file)
        
        self.dict.update(words_to_add)
        self.dict.difference_update(words_to_remove)
        self.save()
