# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


user_input = input("Enter words: ")

x = user_input.split(" ")
print(x)

result_list = []
for i in x:
    tuple(i)
    print(tuple(i))
    result_list.append(tuple(i))
print(result_list)

    

