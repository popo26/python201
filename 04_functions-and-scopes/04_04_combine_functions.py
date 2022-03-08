# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.

def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(name, text, greet_param):
    greeting = greet(greet_param, name)
    letter = f"\n{name} \n{text}"
    return greeting + letter

print(write_letter("Ramon", "Hope you have a nice day", "Hello"))