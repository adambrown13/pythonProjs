import re

file_name = 'wordsEn.txt'

with open(file_name) as f:
    output = f.readlines()
total_words = [x.strip() for x in output]

approved_letter = re.compile("^[^acefghjkrsyz]+$")
trimmed_words = filter(approved_letter.match, total_words)

print(list(trimmed_words))

