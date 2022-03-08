# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

#With Enumerate
def my_enumerate(items):  # add your arguments
      # add your code implementation
      for index, char in enumerate(items):
            print(index, char)

list_ = ["tomato", "dog", "cat"]
print(my_enumerate(list_))

#Withrange(len(items))

def my_enumerate2(items):
      for index in range(len(items)):
            print(f"{index}; {items[index]}")

print(my_enumerate2(list_))
