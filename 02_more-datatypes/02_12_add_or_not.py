# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

is_running = True
points = 5
import sys

while is_running:
    num_list = []
    for user_input in range(0, 50):
            user_input = int(input("Enter a number: "))
            # print(type(user_input))
            if user_input not in num_list:
                num_list.append(user_input)
                print(num_list)
                num_set = set(num_list)
                print(num_set)
                print(points)
            else:
                points -= 1
                print(points)
                if points == 0:
                    sys.exit()

            



    
    


    

