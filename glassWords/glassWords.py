"""
Words that, if you wrote them on a piece of glass in a certain font, would look like an
English word on the flip side
"""

import re

file_name = 'wordsEn.txt'

with open(file_name) as f:
    output = f.readlines()
total_words = [x.strip() for x in output]

approved_letter = re.compile("^[^acefghjkrsyz]+$")
flip_trimmed_words = map(lambda x: x[::-1], filter(approved_letter.match, total_words))  

final_words = []

quickcheck = False

for word in flip_trimmed_words:
    new_word = ""
    for c in word:
        if c == "b":
            new_word += "d"
        elif c == "d":
            new_word += "b"
        elif c == "p":
            new_word += "q"
        elif c == "q":
            new_word += "p"
        else:
            new_word += c
    if new_word in total_words:
        final_words.append(new_word)


print (final_words)
