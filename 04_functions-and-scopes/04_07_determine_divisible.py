# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def can_divide_either(num):
    result_or =  num % 4 == 0 or num % 7 == 0
    return result_or

def can_devide_both(num):
    result_and = num % 4 == 0 and num % 7 == 0
    return result_and

num = int(input("Enter a number between 1 and 1,000,000,000: "))

four_or_seven = can_divide_either(num)
four_and_seven = can_devide_both(num)

print(f"the number {num} is {four_or_seven} for division by 4 or 7, and {four_and_seven} for division by 4 and 7.")


