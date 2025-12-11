import os

class DictionaryUpdater:
    def __init__(self, wordfile):
        self.wordfile = wordfile
        self.dict = self.load()

    def is_exclude_word(self, word):
        return False

    def load(self):
        dict = set()
        with open(self.wordfile, 'r') as source:
            for line in source:
                word = line.strip().lower()

                if self.is_exclude_word(word):
                    continue

                dict.add(word)
        return dict

    def save(self):
        tmp_file = f"{self.wordfile}.tmp"

        # output is a sorted unique list of words
        with open(tmp_file, "w") as out:
            for word in sorted(self.dict):
                out.write(f'{word}\n')

        try:
            os.rename(tmp_file, self.wordfile)
        except FileNotFoundError:
            print(f"Error: '{tmp_file}' was not found.")
        except OSError as e:
            print(f"Error renaming {tmp_file} to {self.wordfile}: {e}")
