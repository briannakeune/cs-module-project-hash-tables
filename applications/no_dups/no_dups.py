import re


def no_dups(s):
    cache = {}
    no_dups_string = ''
    words = s.split()
    for index, word in enumerate(words):
        if cache == {}:
            cache[word] = word
            no_dups_string += word

        if word not in cache:
            cache[word] = word
            no_dups_string += ' ' + word

    return no_dups_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups(
        "spam spam spam eggs spam sausage spam spam and spam"))
