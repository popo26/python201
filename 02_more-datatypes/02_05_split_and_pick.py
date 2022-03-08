# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

user_input = input("Enter a word: ")
word_list = user_input.split(" ")

print(word_list)

sets = []
for x in word_list:
    print(set(x))
    sets.append(set(x))
    print(sets)

output = (set[0].intersection(*sets[1:]))
print(output)




