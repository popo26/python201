# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

# 1. Convert to a different data type

list_str = " ".join(str(n) for n in list_)
print(list_str)
print(type(list_str))


# 2. Use a loop and a second list to solve it more manually
list_without_duplicate = []
for char in list_str:
    if list_str.count(char) == 1:
        if char not in list_without_duplicate:
            list_without_duplicate.append(char)
print(list_without_duplicate)

for index in range(len(list_without_duplicate)):
    list_without_duplicate[index] = int(list_without_duplicate[index])
print(list_without_duplicate)



