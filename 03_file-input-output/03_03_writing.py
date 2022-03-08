# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

file = open("03_file-input-output\words.txt")

lines = file.readlines()

for line in reversed(lines):
    # print(line)
    reversed_words = open(r"03_file-input-output\reversed_words.txt", "a")
    reversed_words.write(line)
    reversed_words.close()
file.close()

    


