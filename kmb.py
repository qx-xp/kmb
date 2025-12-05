#!/usr/local/bin/python3.14
#
# word finder for the kmb app1933 English game
#

from dictionary.kmb_dictionary import KMBDictionary

def main():
    dict = KMBDictionary()
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
