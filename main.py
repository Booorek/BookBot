import string


def sort_on(dict):
    return list(dict.values())[0]


def book_words(text):
    words = text.split()
    return len(words)


def word_occurrences(text):
    dict = {}
    letters = [letter for letter in text]
    for letter in letters:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict


with open('books/frankenstein.txt') as f:
    file_contents = f.read()

word_dict = word_occurrences(file_contents.lower())
list_of_dicts = [{key: value} for key, value in word_dict.items() if key in string.ascii_lowercase]

list_of_dicts.sort(reverse=True, key=sort_on)

for _ in list_of_dicts:
    for key, value in _.items():
        print(f"The '{key}' character was found {value} times")

