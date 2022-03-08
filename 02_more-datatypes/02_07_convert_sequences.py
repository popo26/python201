# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tup = tuple(string)
print(tup)

lis =  list(tup)
print(lis)

new_word_list = []
for word in lis:
    new_word = word.replace("c", "k")
    new_word_list.append(new_word)
print(new_word_list)

tup2 = tuple(new_word_list)
print(tup2)
        

