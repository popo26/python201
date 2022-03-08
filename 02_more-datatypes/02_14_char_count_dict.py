# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

user_input = input("Enter a word: ")
dict = {}

for char in user_input:
    n = 1
    print(char)
    if char in dict:
        n += 1
        dict.update({ char: n})
    else:
        dict.update({ char: n})  
    print(dict)

