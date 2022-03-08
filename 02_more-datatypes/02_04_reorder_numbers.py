
# Read in 10 numbers from the user.

# Place all 10 numbers into an list in the order they were received.

user_input = input("Enter 10 numbers with \" space \": ")
print(user_input)

split_user_input = user_input.split(" ")
print(split_user_input)
print(type(split_user_input))

# print(user_input)
number_list = list(split_user_input)
print(number_list)

# for n in number_list:
#     if " " in number_list:
#         number_list.remove(" ")
# print(number_list)

# integer_map = map(int, number_list)
# print(integer_map)
# integer_list = list(integer_map)
# print(integer_list)

# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1





# for index in range(0, len(number_list)):
#     number_list[index] = int(number_list[index])
# print(number_list)
# new_list = " ".join([item for item in number_list])
# print(new_list)



# at the moment only 1 digit number works

#1 2 3 4 5 6 7 8 9 10



