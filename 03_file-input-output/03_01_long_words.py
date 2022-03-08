# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

file = open("03_file-input-output\words.txt")

for word in file:
    if len(word) > 20:
        print(word)

file.close()
