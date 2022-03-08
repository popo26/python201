# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

import random

def generate_num():
    num_list = [1,2,3,4,5,6,7]
    random_num = random.choice(num_list)
    return random_num

def addition(num):
    random_num = generate_num()
    sum = num + random_num
    return sum

# def subtraction(num):
#     add_value = addition(num)
#     remainder = add_value - num
#     return remainder

def multiply(num):
    multipied_num = addition(num) * num
    return multipied_num

answer = multiply(5)
print(answer)




