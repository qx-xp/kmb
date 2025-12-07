class Dictionary:
    default_wordfile = "words_alpha.txt"

    def __init__(self, wordfile=default_wordfile):
        self.wordfile = wordfile
        self.dict = self.load(self.wordfile)

    # define the conditions to exclude certain words
    # from the dictionary index
    # return True to skip a word
    def can_skip(self, word):
        print ("DEBUG: parent can_skip called!")
        return False

    # dictionary key is the sorted characters of a word
    def search_key(self, word):
        char_list = list(word.lower())
        char_list.sort()
        return "".join(char_list)
    
    # create a dictionary where the key is the
    # ordered string of characters, and the value
    # is a list of words that can be spelled by
    # the characters.
    def load(self, wordfile):
        dict = {}
        with open (wordfile) as f:
            for line in f:
                word = line.strip().lower()

                if self.can_skip(word):
                    continue

                key = self.search_key(word)

                if not key in dict:
                    dict[key] = []
                dict[key].append(word)

        return dict


    # return a list of words that can be formed
    # with the string of characters
    def find(self, string):
        key = self.search_key(string)
        if not key in self.dict:
            return []
        return self.dict[key]

    def __str__(self):
        return f"This dictionary is sourced from {self.wordfile}"
