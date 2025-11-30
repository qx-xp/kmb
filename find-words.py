#!/usr/local/bin/python3.14
#
# word finder for the kmb app1933 English game
#
import re

class Dictionary:
    default_wordfile = "words_alpha.txt"

    def __init__(self, wordfile=default_wordfile):
        self.wordfile = wordfile
        self.dict = self.load(self.wordfile)

    # create a dictionary where the key is the
    # ordered string of characters, and the value
    # is a list of words that can be spelled by
    # the characters.
    def load(self, wordfile):
        dict = {}
        with open (wordfile) as f:
            for line in f:
                word = line.strip().lower()

                # ignore non-alphabets
                if not re.search(r"^[a-z]+$", word):
                    continue

                # ignore words longer than 12 chars
                if len(word) > 12:
                    continue

                char_list = list(word)
                char_list.sort()
                word_key = "".join(char_list).lower()

                if not word_key in dict:
                    dict[word_key] = []
                dict[word_key].append(word)

        return dict


    # return a list of words that can be formed
    # with the string of characters
    def find(self, string):
        char_list = list(string)
        char_list.sort()
        word_key = "".join(char_list).lower()

        if not word_key in self.dict:
            return []
        return self.dict[word_key]

    def __str__(self):
        return f"This dictionary is sourced from {self.wordfile}"


def main():
    dict = Dictionary()
    print (dict)

    while True:
        try:
            line = input(">>> ")
            string = line.strip()
            for match in dict.find(string):
                print(match)
        except EOFError:
            break
        except Exception as e:
            print (f"{e}")
            break


if __name__ == "__main__":
    main()
